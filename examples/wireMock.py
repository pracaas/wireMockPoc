# import requests
#
# # 1. Start WireMock server
# wiremock_url = "http://localhost:8082/__admin"
#
# # 2. Set up a stub using WireMock API
# stub_mapping = {
#     "request": {
#         "method": "GET",
#         "url": "/api/books",
#         "headers": {
#             "Content-Type": {
#                 "equalTo": "application/json"
#             }
#         }
#     },
#     "response": {
#         "status": 200,
#         "headers": {
#             "Content-Type": "application/json"
#         },
#         "body": {
#             "books": [
#                 {
#                     "id": 1,
#                     "title": "Book 1"
#                 },
#                 {
#                     "id": 2,
#                     "title": "Book 2"
#                 }
#             ]
#         }
#     }
# }
#
# stub_mapping_url = f"{wiremock_url}/mappings/new"
# response = requests.post(stub_mapping_url, json=stub_mapping)
# response.raise_for_status()
#
# # 3. Make a request to the mocked service
# books_url = "http://localhost:8082/api/books"
# response = requests.get(books_url, headers={"Content-Type": "application/json"})
# response.raise_for_status()
#
# # 4. Validate the response from the mock
# json_response = response.json()
# print(json_response)
# # Output: {'books': [{'id': 1, 'title': 'Book 1'}, {'id': 2, 'title': 'Book 2'}]}
#
# # 5. Stop WireMock server (optional)
# stop_url = f"{wiremock_url}/shutdown"
# requests.post(stop_url)
