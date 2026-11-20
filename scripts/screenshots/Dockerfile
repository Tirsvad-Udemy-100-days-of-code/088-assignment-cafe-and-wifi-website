# Image that takes the screenshots of the website with a headless browser.
# It only exists to keep the host desktop free (framework/process/gui-testing.md).
FROM python:3.13-slim-bookworm
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PLAYWRIGHT_BROWSERS_PATH=/ms-playwright \
    PYTHONDONTWRITEBYTECODE=1
RUN python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir playwright==1.49.1 \
    && python -m playwright install --with-deps chromium
WORKDIR /work
