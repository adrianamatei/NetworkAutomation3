# import requests
# from gns3fy.projects import Project
# from gns3fy.connector import Connector
#
# BASE_URL = "http://92.81.55.146:3080"
# server = Connector(url=BASE_URL)
#
# project = Project(
#     connector=server,
#     name="Matei Adriana Ionela",
#     project_id="096a88ee-d93f-4beb-be18-75797ba59e07"
# )
# project.get()
# project.open()
#
# # înlocuiește cu template_id-ul real găsit la pasul 1
# TEMPLATE_ID = "12345678-90ab-cdef-1234-567890abcdef"
#
# resp = requests.post(
#     f"{BASE_URL}/v2/projects/{project.project_id}/nodes",
#     json={
#         "name": "Router2",
#         "template_id": TEMPLATE_ID,
#         "x": -538.0,
#         "y": 1.0
#     }
# )
#
# print("Status:", resp.status_code)
# print("Nod creat:", resp.json())

from gns3fy import Gns3Connector, Project, Node


def main():
    server = Gns3Connector("http://92.81.55.146:3080")

    project = Project(project_id="096a88ee-d93f-4beb-be18-75797ba59e07", connector=server)
    project.get()

    node = Node(
        project_id=project.project_id,
        connector=server,
        name="IOSv2",
        template="Cisco IOSv 15.9(3)M6",
        x=0,
        y=0
    )
    try:
        node.create()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
