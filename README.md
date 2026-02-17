# group11112025Project

/backend   uv add "fastapi[standard]"


/backend/app uv run -m uvicorn main:app
/backend/app uv run -m uvicorn main:app  --reload

docker compose up  --build
docker compose up

http://localhost:19999/docs
http://localhost:20000/docs

-    ~/Desktop/group11112025Project/backend/app    libs !4 ···· ✔  backend   3.12    19:31:58  
╰─ uv run alembic init migrations
- inside docker container
╰─ alembic revision --autogenerate -m 'init'
- inside docker container
╰─ alembic upgrade head
- inside docker container
╰─ alembic downgrade -1