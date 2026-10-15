# Engineering decisions and trade-offs

## 1. Reconciling multiple sources
**Problem:** ERP inventory and monitoring records can disagree or contain duplicate/incorrect identifiers.

**Approach:** Keep ERP and monitoring as distinct sources, normalize identifiers for matching, and expose mismatches for review. In the web import flow, permit rows to be excluded before synchronization.

**Trade-off:** Human review introduces a step but reduces incorrect records being reactivated.

## 2. Monitoring state transitions
**Problem:** A single current status cannot show how long a device was unhealthy or when it recovered.

**Approach:** Maintain snapshots and significant transition events. Derive operational indicators using status and elapsed time rather than counting all non-collecting records alike.

**Trade-off:** Additional processing and history storage, balanced by better field prioritization.

## 3. Field-first map performance
**Problem:** Displaying every device marker is visually noisy and costly on basic phones.

**Approach:** Focus the map on problematic locations and a limited nearby set. Cluster related markers and show the technician's position.

**Trade-off:** The map is optimized for diagnostics, not a full inventory map.

## 4. Web account management
**Problem:** The application needs accounts outside the corporate directory without opening unrestricted self-registration.

**Approach:** Explicitly authorize invited identities; assign roles, support first-access setup, hashed passwords, session-version invalidation and protections against repeated failed sign-ins.

**Trade-off:** Manual authorization requires operational ownership and timely revocation. Roles must be enforced by the API.

## 5. External navigation vs geocoding
**Problem:** A record with an ERP address may lack stored latitude and longitude.

**Consideration:** A navigation deep link can pass the full address to a maps app without requiring geocoding in the product backend. Stored coordinates remain useful for internal maps and clustering.

**Status:** Design opportunity; do **not** confuse it with a deployed REP-Monitor feature.

## 6. Operational validation
The team used incremental tests, field feedback, SQL verification and iterative deployment. Documentation should distinguish **implemented**, **tested**, and **planned** behavior. No unsupported latency, savings or uptime claims are made in this case.
