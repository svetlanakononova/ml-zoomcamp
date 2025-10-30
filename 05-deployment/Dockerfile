# Use the official Python 3.13.5 slim version based on Debian Bookworm as the base image
FROM agrigorev/zoomcamp-model:2025
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /code
COPY "pyproject.toml" "uv.lock" ".python-version" ./
RUN uv sync --locked
ENV PATH="/code/.venv/bin:$PATH"

COPY pipeline_v1.bin .


COPY "predict.py" .

EXPOSE 9697

ENTRYPOINT ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "9697"]