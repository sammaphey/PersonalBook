FROM python:3.11

RUN pip install --user poetry
ENV PATH="${PATH}:/root/.local/bin"

RUN python -m venv .venv
RUN . .venv/bin/activate
    
COPY api/ ./api

WORKDIR /api


RUN poetry install

EXPOSE 5000

ENTRYPOINT [ "poetry", "run", "api", "launch" ]
