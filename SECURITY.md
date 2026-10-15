# Public portfolio security and disclosure policy

This repository is a **public case study** and must not be used to distribute proprietary software or production information.

Never commit:
- Production source code or copied configuration without explicit rights to publish
- Secrets, tokens, passwords, keys, JWTs, database connection strings or live service URLs
- Names, email addresses, user IDs, employee data, device serials and customer data
- Internal IP addresses, DNS names, cloud project/tenant identifiers, or access-control details
- Unredacted screenshots, maps, database exports and real logs

Use fictional records and neutral hostnames such as `example.invalid`. Sanitization should be reviewed before every publication, especially of images, git history and metadata. Sanitized examples are **illustrative** and are not presented as copies of production source.

A public demo should use a separate account/project, synthetic dataset, restrictive IAM and no connectivity to private production systems.

Report a sensitive disclosure privately to the repository owner rather than posting it as a public issue.
