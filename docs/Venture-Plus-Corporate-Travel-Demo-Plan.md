# Venture Plus × Specialist Services
## Corporate Travel Management — Demo Plan (Prototype with Dummy Data)

---

## 1. Demo Objective

Demonstrate a centralized corporate travel portal where the full journey is managed in one place:

**Employee Request → Approval → Travel Desk → Smart Options → Selection → Booking → Traveler Profile/Preferences → Complete Itinerary → Management Visibility**

**Core message:** HR does not need to chase emails, compare screenshots, repeatedly provide traveler information, check whether seats/meals/reward numbers were added, or manually track everyone's travel. Everything is visible and managed from one place.

- **Client:** Specialist Services
- **Travel execution partner:** Venture Plus (replaces Akbar Travels in the prototype)
- **Final approver:** Chris (President)
- **Data:** All dummy — no real booking or GDS/API integration

---

## 2. Roles in the Demo

The prototype uses a role switcher to walk through each persona:

| Role | Responsibility |
|------|----------------|
| **Employee** | Raise travel request, review options, view itinerary |
| **Chris (President)** | Final approval and over-band reconfirmation |
| **Venture Plus Travel Desk** | Pick up approved requests, present options, confirm bookings |
| **HR (Melissa)** | Governance, visa oversight, traveler tracker |
| **Management** | Spend dashboard and traveler visibility |

---

## 3. Dummy Traveler Profiles (Pre-loaded)

Profiles are stored once and applied automatically to every booking.

| Name | Role | Travel Class | Seat | Meal | Loyalty Program |
|------|------|--------------|------|------|-----------------|
| Chris Ridley | President | Business | Aisle | Standard | Emirates Skywards |
| Melissa Payumo | HR Director | Premium Economy | Aisle | Vegetarian | KLM Flying Blue |
| Kyle Morrison | VP Sales | Premium Economy | Window | Non-vegetarian | Emirates Skywards |
| Sarah Ahmed | Sales Executive | Economy | Aisle | Vegetarian | — |
| Raj Patel | Project Engineer | Economy | Aisle | Vegetarian | Air India |

Each profile also holds passport number, nationality, date of birth, and travel class eligibility. These details are never re-entered per trip.

### Travel Class Rules

| Tier | Class |
|------|-------|
| Chris (President) | Business |
| VP level, Kyle, Melissa | Premium Economy (where available) |
| All other staff | Economy |
| Chris (short-haul) | Budget airlines acceptable; night flights for morning arrival |

---

## 4. Regional Cost Bands (Dummy Policy)

| Region | Flight Threshold (AED) | Hotel Nightly Threshold (AED) |
|--------|------------------------|-------------------------------|
| GCC | 3,000 | 600 |
| Europe | 5,000 | 900 |
| Asia | 3,500 | 450 |
| Rest of World | Case-by-case | Case-by-case |

- Bookings within band proceed automatically.
- Over-band bookings are paused and escalated to Chris for reconfirmation before ticket issuance.

---

## 5. End-to-End Demo Flow

```
Employee submits individual travel request
        ↓
Request routes for approval
        ↓
Chris approves (no booking activity before this)
        ↓
Venture Plus travel desk automatically notified
        ↓
        ┌── Visa required? ──┐
        │ YES                │ NO
        ↓                    ↓
Travel Hub checklist    Present structured options
Document upload         (flights / hotel / car)
HR: NOC + salary cert
Visa approved (hard gate)
        ↓                    ↓
        └────────┬───────────┘
                 ↓
        Traveler / desk selects option
                 ↓
        Within cost band?
        ├── YES → Booking confirmed
        └── NO  → Flag HR → Chris reconfirms → Booking confirmed
                 ↓
        Itinerary issued (trip-named documents)
        Preferences auto-applied (seat, meal, loyalty)
        HR and traveler notified
        Management dashboard updated
```

### Hard Rules Demonstrated

1. No booking activity until Chris approves.
2. If visa is required: no ticket and no booking work until visa is fully secured.
3. One travel request form per traveler (no combined group forms).
4. Approved form is the single source of instruction — travel desk does not deviate from it.

---

## 6. Demo Scenarios

### Scenario A — Standard Trip (Primary Demo Path)

**Message:** No emails, no screenshots, preferences auto-applied.

**Step 1 — Employee submits request**

Sarah Ahmed logs in and creates a new travel request:

| Field | Value |
|-------|-------|
| Traveler | Sarah Ahmed |
| Department | Sales |
| Department Head | Kyle Morrison |
| Purpose | Client visit |
| Project / Client | Project #SS-2026-NL-04 — H2M Montfoort |
| Origin | Dubai (DXB) |
| Destination | Amsterdam (AMS) |
| Departure date | 12 September 2026 |
| Preferred departure timing | Late afternoon / early evening |
| Return date | 15 September 2026 |
| Preferred return timing | Afternoon (full client day) |
| Hotel required | Yes — near Montfoort |
| Check-in / Check-out | 12 Sep / 15 Sep |
| Car required | No |
| Visa required | No |
| Status after submit | Pending Chris approval |

**Step 2 — Chris approves**

Chris opens the approval inbox, reviews the request, and approves.

- Venture Plus travel desk is automatically notified.
- HR receives a copy (simulated notification to travel@specserve.com).
- Approved form becomes the instruction set for booking.

**Step 3 — Venture Plus presents structured options**

Travel desk opens work queue and picks up request **TR-1042**.

System pulls Sarah's profile: Economy class, aisle seat, vegetarian meal.

**Flight options (structured — not screenshots):**

| Option | Airline | Route | Depart | Arrive | Duration | Price (AED) | Band Status |
|--------|---------|-------|--------|--------|----------|-------------|-------------|
| A — Recommended | KLM | Direct DXB–AMS | 16:45 | 21:30 | 7h | 4,200 | Within Europe band (5,000) |
| B | Emirates | Direct DXB–AMS | 14:20 | 19:05 | 7h | 4,650 | Within band |
| C | Qatar Airways | 1 stop via DOH | 11:00 | 20:15 | 10h | 3,800 | Within band |

Option A is marked as the consultant recommendation: matches preferred timing, direct route, best overall value for the trip requirement.

**Hotel options:**

| Hotel | Location | Rate/Night (AED) | Band Status |
|-------|----------|------------------|-------------|
| Crowne Plaza Utrecht | Near Montfoort | 820 | Within Europe band (900) |
| Hilton Utrecht Central | City centre | 880 | Within band |

**Step 4 — Selection and booking**

Sarah (or travel desk on her behalf) selects KLM flight + Crowne Plaza Utrecht.

Booking confirmed with auto-applied preferences:
- Aisle seat
- Vegetarian meal
- Traveler profile on file

**Step 5 — Complete itinerary**

Final itinerary displayed with clearly named documents:

`Sarah Ahmed – Amsterdam – Sep 2026 – KLM Ticket`  
`Sarah Ahmed – Amsterdam – Sep 2026 – Hotel Voucher`

Hotel payment status: **Confirmed / Paid** — no check-in surprises.

HR notified. No chasing required.

---

### Scenario B — Visa Gate

**Message:** No ticket until visa is secured — hard rule with no exceptions.

**Step 1 — Request with visa**

Raj Patel submits:
- Dubai → Frankfurt
- Visa required: Yes (Germany, Indian passport)
- Chris approves

**Step 2 — Booking locked**

System displays: **Booking locked — visa pending**

Travel Hub checklist shown:
- Valid passport copy
- ID photo
- Completed visa information form
- Client invitation letter (if required)
- NOC from HR
- Salary certificate from HR

**Step 3 — Visa process**

- Raj uploads required documents.
- HR issues NOC and salary certificate (simulated).
- Venture Plus verifies documents against visa matrix.
- Visa status updated to: **Approved**

**Step 4 — Booking unlocks**

Booking gate opens. Travel desk proceeds with flight and hotel arrangements per the approved form.

---

### Scenario C — Over-Band Escalation

**Message:** Policy enforced; exceptions documented and auditable.

**Step 1 — Request**

Kyle Morrison submits:
- Dubai → Singapore
- Asia flight band: AED 3,500

**Step 2 — Over-band flag**

Only viable direct option: AED 4,100 (last-minute, no cheaper direct available).

System flags: **Over band — Chris reconfirmation required**

**Step 3 — Escalation and approval**

Chris reviews with documented rationale: *"Client meeting — no cheaper direct flight available."*

Chris reconfirms. Booking proceeds. Rationale saved in audit trail.

---

## 7. HR and Management Screens

### Traveler Safety Tracker

Consolidated view of who is traveling — critical for employee safety and emergency management.

| Traveler | Current Location | Return Date | Status |
|----------|------------------|-------------|--------|
| Sarah Ahmed | Amsterdam, Netherlands | 15 Sep 2026 | In transit |
| Kyle Morrison | Singapore | 20 Sep 2026 | In transit |
| Chris Ridley | Dubai, UAE | — | Local |

### Spend Dashboard (YTD — Dummy)

| Metric | Value |
|--------|-------|
| Total travel spend | AED 487,000 |
| By region — GCC | 35% |
| By region — Europe | 40% |
| By region — Asia | 20% |
| By region — Rest of World | 5% |
| Over-band incidents | 2 (both approved with rationale) |

### Audit Trail (per trip)

Full record maintained for compliance:

Request submitted → Manager acknowledged → Chris approved → Options presented → Option selected → Booking confirmed → Itinerary issued

---

## 8. Key Messages for the Client

| # | Message |
|---|---------|
| 1 | One travel request form per traveler — no messy combined group forms |
| 2 | Chris approves — nothing moves until approval is complete |
| 3 | Venture Plus travel desk receives approved requests automatically |
| 4 | Flight options presented in a clean, structured format — not email screenshots |
| 5 | Traveler preferences (seat, meal, loyalty, passport) stored once and applied every time |
| 6 | Regional cost bands enforced — over-band bookings escalate to Chris |
| 7 | Visa requirement is a hard gate — no booking until visa is secured |
| 8 | Travel documents clearly named by trip — not generic filenames |
| 9 | Hotel payment confirmed before the traveler arrives |
| 10 | HR governs and oversees — HR does not coordinate every email |
| 11 | Management has spend visibility and live traveler tracking for safety |

---

## 9. Venture Plus Value Proposition vs Current Model

| Current Model (Akbar + Email) | Venture Plus Portal |
|-------------------------------|---------------------|
| Flight options sent as screenshots | Structured, comparable option cards |
| Passport and details re-requested every trip | Profile stored once, used every time |
| Repeated reminders to book aisle seats | Preferences auto-applied from profile |
| Generic ticket filenames (e.g. "Chris Ridley.pdf") | Trip-labeled documents |
| HR relays messages between staff and agency | Travel desk works directly from approved form |
| Excel export for who is traveling | Live traveler safety tracker |
| Informal cost discussions | System-enforced bands with documented escalation |
| Hotel voucher issues at check-in | Payment status visible before arrival |
| No structured consultant recommendation | Best overall option highlighted with rationale |

---

## 10. What the Prototype Does Not Include

| Item | Notes |
|------|-------|
| Real flight/hotel inventory | Dummy data only; agency/API integration later |
| Live booking or payment | Simulated confirmation only |
| Full visa matrix (all countries/nationalities) | Sample destinations for demo |
| Finance invoice reconciliation | Background context only |
| Email auto-extraction to tickets | Optional future enhancement |
| Centurion system integration | Standalone portal for prototype |
| GL code assignment | Mentioned in form; ownership TBD |
| Real corporate rate negotiation | Shown as future value with dummy badges |

---

## 11. Suggested Demo Walkthrough Order

1. **Opening** — State the problem: email chains, screenshots, HR as relay, repeated traveler data entry.
2. **Scenario A** — Full end-to-end happy path from request to itinerary.
3. **Scenario B** — Visa gate: show booking locked until visa approved.
4. **HR / Management screens** — Traveler safety tracker and spend dashboard.
5. **Scenario C** — Over-band escalation with Chris reconfirmation.
6. **Closing** — HR stops being the relay; Venture Plus runs the travel desk from one governed portal.

---

## 12. Technical Approach (Prototype)

- Web application with role switcher for demo personas
- Dummy JSON data for travelers, flights, hotels, and requests
- Venture Plus branding throughout; Specialist Services as end client
- Deployable URL for live demonstration or screen share

---

## 13. Open Points for Confirmation

| # | Question |
|---|----------|
| 1 | Build full flow (request → approval → booking) or start at approved request only? |
| 2 | Include email simulation to travel@specserve.com? |
| 3 | Any specific destinations or travelers Melissa wants reflected in dummy data? |
| 4 | Demo format: deployed URL or screen share? |

---

*Document prepared for Venture Plus — Specialist Services Corporate Travel Management prototype demonstration.*
