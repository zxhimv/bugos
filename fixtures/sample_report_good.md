# Summary
Manual read-only authorization check indicates that Demo User B can access Demo User A account metadata through an object identifier.

# Location
https://app.demo.example/account/123 and endpoint GET /api/accounts/123

# Affected parties
Any demo tenant account whose numeric object identifier can be guessed by another authenticated demo account.

# Impact
Unauthorized read access to account metadata could expose business profile information. No destructive action, credential access, or customer data access was attempted.

# Steps to reproduce
1. Sign in as owned demo account A and note object id 123.
2. Sign in as owned demo account B in a separate browser profile.
3. Send GET /api/accounts/123 as account B.
4. Observe account A metadata in the response. Evidence E01 shows the response with synthetic values only.

# Parameters
Path parameter: account id in /api/accounts/{id}.

# Proof of Concept / Evidence
E01: synthetic_request_response.txt with redacted request and response.

# Remediation
Enforce object-level authorization server-side for every account lookup and verify requester-to-resource ownership before returning data.
