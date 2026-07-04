#!/bin/bash

set -e

uvicorn app.api.server:app --reload