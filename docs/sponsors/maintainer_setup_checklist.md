# GitHub Sponsors Maintainer Setup Checklist

Status: draft for human review

This checklist is for manual setup outside the repository. Do not commit payout, tax, identity, billing, card, bank, PayPal account, or private sponsor data to the repository.

## Repository Setup

- [ ] `.github/FUNDING.yml` exists on the default branch.
- [ ] Funding config uses GitHub Sponsors and the reviewed public PayPal seller QR-code payment URL only.
- [ ] README explains sponsorship boundaries.
- [ ] Sponsor language does not imply target testing, scanning, exploitation, payloads, credentials, report submission, or guaranteed outcomes.
- [ ] PayPal is presented only as a public funding URL, not as checkout automation.

## GitHub Sponsors Account Setup

Complete manually in GitHub:

- [ ] Check eligibility for GitHub Sponsors.
- [ ] Enable GitHub Sponsors for the correct account.
- [ ] Complete identity checks if required.
- [ ] Complete payout setup.
- [ ] Complete tax forms.
- [ ] Review public sponsor profile.
- [ ] Review sponsor tier text before publishing.
- [ ] Confirm cancellation/refund expectations.

## PayPal Account Setup

Complete manually in PayPal:

- [ ] Confirm the public PayPal QR-code/payment link points to the intended account.
- [ ] Complete identity checks directly in PayPal if required.
- [ ] Complete payout setup directly in PayPal.
- [ ] Review fees, disputes, refunds, reserves, and account limits.
- [ ] Confirm bookkeeping and tax treatment with the relevant adviser.
- [ ] Do not commit PayPal login, payout, card, bank, tax, identity, billing, or transaction data.

## Tax / Legal / Privacy Review

Before promotion:

- [ ] Tax treatment reviewed.
- [ ] Public sponsor wording reviewed.
- [ ] PayPal public-link use reviewed.
- [ ] Benefits do not create unsafe service obligations.
- [ ] No private customer data is accepted through sponsorship.
- [ ] No sponsor benefit implies real target work.
- [ ] No sponsor benefit implies guaranteed findings, payouts, revenue, or report acceptance.

## No-Go Items

Never commit:

- payout account details
- tax identification numbers
- identity documents
- card or bank details
- PayPal login or private account details
- billing records
- private sponsor messages
- customer data
- secrets, tokens, cookies, or credentials

## Safe Promotion Draft

`Support bugos: conservative, offline-first tooling for safer security workflow preparation.`

## Unsafe Promotion Examples

Do not use:

- sponsor bug bounty automation
- sponsor exploit development
- sponsor target testing
- sponsor guaranteed bounty results
- sponsor report submissions

## Final Manual Gate

Before promoting sponsorship publicly, confirm:

- repository wording is safe
- GitHub Sponsors account is active or intentionally pending
- PayPal public link resolves to the intended account
- tax/payout setup is complete
- benefits are reviewed
- no unsafe capability is promised
