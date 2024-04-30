FROM python:3.11

WORKDIR /app/

ENV POETRY_HOME=/opt/poetry
ENV PATH="$POETRY_HOME/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# タイムゾーンを日本時間に設定
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN curl -sSL https://install.python-poetry.org | python -

RUN pip install poetry==1.8.2

COPY pyproject.toml poetry.lock /app/

RUN poetry install --no-root

COPY app /app/app

COPY README.md /app/

RUN poetry install 


CMD ["poetry", "run", "uvicorn", "app.main:router", "--host", "0.0.0.0", "--port", "8000", "--reload"]