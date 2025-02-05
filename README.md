## <div align="center">Documentation</div>

簡単にIoTのシステムを構築するサンプルソースコードを保管しています。<br>
⚠️ **注意:** ご自身の環境で構築する場合は、`user名` や `password` などの変数を変更してお使いください。


## 開発環境
FrontEnd: -<br>
BackEnd: FastAPI<br>
ORM: SQLAlchemy<br>
DB: PostgreSQL<br>


## DockerのACCESS権設定
docker_data/のアクセス権に注意<br>
(例) sudo chmod -R 777 ./docker_data/pgadmin<br>
(例) sudo chmod -R 777 ./docker_data/postgres/pgdata<br>


## アプリ立ち上げ
1. Clone the repository

  ```bash
   git clone https://github.com/akihiko-ima/fastapi-iot-sample.git
  ```

2. Install dependencies

  ```bash
   python3 -m venv env_fastapi
   source ./env_fastapi/bin/activate
   pip3 install -r requirements.txt
  ```

3. Run the development server

  ```bash
   uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
  ```

- requirements.txt<br>
  pip install -r requirements.txt<br>
  pip freeze > requirements.txt


## Alembicによるマイグレーション
1. 必要なライブラリをインストール<br>
  ```bash
  pip install alembic psycopg2-binary
  ```

2. Alembicの初期化<br>
  ```bash
  alembic init migrations
  ```

3. alembic.iniファイルのDB接続設定を変更<br>
  該当箇所<br>
  ```alembic.ini
  sqlalchemy.url = driver://user:pass@localhost/dbname
  ```

4. migrations/env.pyファイルのDB設定を変更<br>
  ```env.py
  from models import Base           # 新規追加

  target_metadata = Base.metadata   # Alembicにモデルの内容を知らせる
  ```

5. migrationファイルの作成<br>
  マイグレーションメッセージは変更可能<br>
  ```bash
  alembic revision --autogenerate -m "create initial table"
  ```

6. データベースへ適用<br>
  ```bash
  alembic upgrade head
  ```
