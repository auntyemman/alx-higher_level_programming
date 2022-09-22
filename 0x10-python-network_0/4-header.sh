#!/bin/bash
# curl sends GET req to URL, displays response body
curl -sH GET "X-School-User-Id: 98" "$1" -X
