1. 프로토콜 버퍼를 이용해 flask 서버와 client(앱 또는 웹) 이 통신하는 것이 가능함.
2. 프로토콜 버퍼에 에러도 정의할 수 있음.
3. flask 소켓을 통해서 사용자 간의 양방향 소켓 통신도 가능함.
4. 앱은 자바 안드로이드, 코틀린, 리액트, 플러터 등으로 개발
5. 웹으로 구현하려면 flask, 리액트, 플러터 3개 중 하나로 개발.
6. proto 파일을 작성하는 문법은 따로 찾아봐야 할 거 같음.
-> 우선 pip install -r requirements.txt 실행해서 라이브러리 설치하고 테스트.

################################################################################################################
flask socket chat example: https://bokyeong-kim.github.io/python/flask/2020/05/09/flask(1).html
flask socket-io: https://pypi.org/project/Flask-SocketIO/

위 예제는 일반 websocket 이지만 아래 threaded socket 라이브러리 보면 thread로 띄우는 것도 가능해보임.
################################################################################################################

flask threaded sockets: https://pypi.org/project/flask-threaded-sockets/
protobuf pypi: https://pypi.org/project/protobuf/