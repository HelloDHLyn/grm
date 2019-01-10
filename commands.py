from terminaltables import AsciiTable

from github import query
from repository import current_repo
from utils import str_shorten, str_break_lines

_QUERY_ISSUE_LIST = """
query {{
  repository(owner: "{}", name: "{}") {{
    issues(first: 20, orderBy: {{field: CREATED_AT, direction: DESC}}) {{
      nodes {{
        number
        title
        state
        updatedAt
      }}
    }}
  }}
}}
"""

_QUERY_ISSUE_LIST_MY = """
query {{
  search(query: "repo:{}/{} assignee:{} is:issue", type: ISSUE, first: 20) {{
    edges {{
      node {{
        ... on Issue {{
          number
          title
          state
          updatedAt
        }}
      }}
    }}
  }}
}}
"""

_QUERY_ISSUE = """
query {{
  repository(owner: "{}", name: "{}") {{
    issue(number: {}) {{
      number
      title
      state
      body
      updatedAt
    }}
  }}
}}
"""


def issue():
    def _print_issue_list(issues):
        table = list(map(lambda n: [n['number'], str_shorten(n['title'], 40), n['state'], n['updatedAt']], issues))
        table.insert(0, ['#', 'Title', 'State', 'Updated'])
        print(AsciiTable(table).table)

    def list_(my=False):
        """
        Get list of issues.

        Flags:
          --my  : filter only my issues
        """
        repo = current_repo()

        if my:
            viewer = query('query { viewer { login } }')['viewer']
            res = query(_QUERY_ISSUE_LIST_MY.format(repo.owner, repo.name, viewer['login']))
            issues = map(lambda e: e['node'], res['search']['edges'])
        else:
            res = query(_QUERY_ISSUE_LIST.format(repo.owner, repo.name))
            issues = res['repository']['issues']['nodes']
          
        _print_issue_list(issues)
    
    def get(number: int):
        """
        Get a issue
        """
        repo = current_repo()
        
        issue = query(_QUERY_ISSUE.format(repo.owner, repo.name, number))['repository']['issue']
        if issue is None:
            raise Exception('Cannot get issue.')

        table = [
          ['#', 'Content'],
          ['Number', issue['number']],
          ['Title', str_shorten("{} ({})".format(issue['title'], issue['state']), 70)],
          ['Body', str_break_lines(issue['body']) or 'Empty'],
          ['Updated', issue['updatedAt']],
        ]
        print(AsciiTable(table).table)

    return {
        'list': list_,
        'get': get,
    }
