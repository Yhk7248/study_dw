from flask import Flask, request, jsonify
import my_proto_pb2

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    # 요청 데이터 역직렬화
    req = my_proto_pb2.Request()
    req.ParseFromString(request.data)

    # 비즈니스 로직 처리
    response = my_proto_pb2.Response()
    response.status = "success"
    response.message = f"Received command: {req.command}"

    # 응답 데이터 직렬화
    return response.SerializeToString(), 200, {'Content-Type': 'application/octet-stream'}


if __name__ == '__main__':
    app.run()
