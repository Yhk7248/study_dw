
import requests
import my_proto_pb2

req = my_proto_pb2.Request()
req.command = "example_command"
req.data = "example_data"

response = requests.post('http://localhost:5000/api', data=req.SerializeToString())

resp = my_proto_pb2.Response()
resp.ParseFromString(response.content)

print(f"Status: {resp.status}, Message: {resp.message}")