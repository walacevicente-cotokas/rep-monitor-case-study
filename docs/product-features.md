# Product tour — mobile and web

## Android (Flutter)
- Authenticated first access and sign-in flows
- Equipment lookup by asset identifier (REP), serial, customer and location
- Device information, last monitoring collection, days without collection and current status
- Technician location and clustered map of nearby problematic locations
- Revalidation action and recent revalidation information
- Overview indicators: recovering vs. not collecting for an extended interval
- Responsive-layout fixes for lower-end phones and tablets

## Web (Next.js)
- Authenticated dashboard and equipment lookup
- Map and operational reports
- User-account administration with role distinctions
- Recovery workflows for application credentials
- Import review before applying ERP inventory updates, including the option to omit rows
- Browser and mobile views share the same backend and database concepts

## Representative workflow
1. A technician searches for an equipment identifier.
2. The client requests the current record via the API.
3. The technician checks monitoring status and last collection time.
4. If appropriate, a revalidation request is sent via an authenticated backend operation.
5. The UI refreshes to reflect the new data.

## Media roadmap
A public demo should use **synthetic data only**. Planned materials: (1) mobile overview screen, (2) device details, (3) cluster map, (4) web dashboard, (5) controlled inventory import review. No existing screenshots are included until reviewed and sanitized.

**Do not share live client addresses, user names, serials, REP lists, customer records or internal URLs.**
