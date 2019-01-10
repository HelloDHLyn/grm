from terminaltables import AsciiTable

from github import query
from repository import current_repo
from utils import str_shorten

_QUERY_ISSUE_LIST = """
query {{
  repository(owner: "{}", name: "{}") {{
    issues(first: 20, orderBy: {{field: CREATED_AT, direction: DESC}}) {{
      nodes {{
        number
        title
        updatedAt
      }}
    }}
  }}
}}
"""


def issue():
    def list_():
        """
        Get list of issues.
        """
        repo = current_repo()

        res = query(_QUERY_ISSUE_LIST.format(repo.owner, repo.name))
        nodes = res['data']['repository']['issues']['nodes']

        table = list(map(lambda n: [n['number'], str_shorten(n['title'], 40), n['updatedAt']], nodes))
        table.insert(0, ['#', 'Title', 'Updated'])
        print(AsciiTable(table).table)

    return {
        'list': list_,
    }
