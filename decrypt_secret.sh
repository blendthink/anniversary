#!/bin/sh

gpg --quiet --batch --yes --decrypt --passphrase="$SECRET_PASSPHRASE" \
--output anniversaries.json anniversaries.json.gpg
