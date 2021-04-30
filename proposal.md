# notes

## Ideas for dev projects

- extract and standardize layout engines
  - let the Figure have a LayoutEngige attribute
  - let it do _what ever it wants_ at draw time
  - can relax fixed figure size!
  - flex-box style layouts
  - r-style "veiw port" based layout
- improve hatching API
  - we think the backends have enough flexibility for arbitarry fill
  - need to add user-facing API code
- path strokes
  - beyond dash pattern
  - arrow heads
  - vary
- 3D improvements
- arrows
- nested tick labels tick labels
- imporved twin/parasite/secondary support

# Proposal

## Proposal purpose

> Limit to one sentence (maximum of 255 characters, including spaces)

> 169 characters

To support the continued maintenance, growth, development, and community
engagement of Matplotlib, the foundational plotting library of the Scientific
Python Ecosystem.


## Propsoal Summary

> A short summary of the application ​(maximum of 250 words) (auto-filled from
> LOI; update if needed)

> 229 words

Matplotlib is the foundational data visualization library for the Scientific
Python Ecosystem, with over a million users, including researchers in
bio-medical imaging, microscopy, and genomics.  For the past 18 years
Matplotlib has been maintained by a vibrant, primarily volunteer, community.
However we have grown too big and widely used to continue on solely volunteer
effort.  For the past 17 months CZI EOSS support for developers has had a
positive effect on the project by complementing and enabling, not replacing,
volunteer work: we propose to continue this effort.

The primary component of the proposed work is the continued maintenance of the
library.  Maintenance tasks are essential for the project's health; though each
individually is small, they are frequently time critical and tedious.  In
addition to on-going and routine maintenance, there are substantial, but
incremental, enhancement to Matplotlib that require long blocks of dedicated
effort to implement. Finally, supported developers improve the management of
the project.  We now have the time and bandwidth to make strategic decisions
about the direction of the project to ensure the long term health and viability
of Matplotlib.

An important part of project management is community management: fostering,
diversifying, and growing our community.  We must ensure that our community is
open and welcoming to everyone who wants to join, with opportunities to
contribute in a spectrum of roles as their interests and skills develop.


## work plan

> A description of the proposed work the applicants are requesting funding for,
> including resources the applicants will provide that are not part of the
> requested funding. For software development-related work (e.g., engineering,
> product design, user research), specify how the work fits into the existing
> software project roadmap.  For community outreach related activities (e.g.,
> sprints, training), specify how these activities will be organized, the
> target audience, and expected outcomes (maximum of 750 words)

The proposed work can be broadly classified into three parts:

- on-going and routine maintenance of Matplotlib;
- implementation of several mid-sized features;
- community and project management.

These tasks are both critical to the long term health of the library and are
difficult, to accomplish well with only volunteers.  These tasks may

The primary component of the proposed work is the continued maintenance of the
Matplotlib.  Maintenance covers a wide range of tasks including triaging and
fixing bugs, reviewing Pull Requests, tagging and building releases, and
keeping the continuous integration services running.  These tasks are essential
for the project's health; though each individually is small, they are
frequently time critical and tedious.  It is unfair and impractical to rely
solely on volunteers to accomplish such tasks.


With only volunteer effort we had an ever growing backlog of Issues and PRs.
This risks missing good ideas and is both discouraging to new contributors and
distracting to the core developers.  In contrast, with CZI support we have
decreased our backlog of open Issues and PRs despite an increase in the number
submitted over the last 15 months.



Examples include fixing long-standing
rendering and performance issues, deep-dive explanatory documentation,
homogenizing and smoothing the API, and new user-facing functionality.
Projects to be pursued with the funding requested here will be selected in
consultation with down-stream biomedical libraries.


This requires dedicated effort, over
long periods of time, beyond what can be sustained by volunteers alone.  We
must ensure that our community is open and welcoming to everyone who wants to
join, with opportunities to contribute in a spectrum of roles as their
interests and skills develop.



We propose to continue full support (1 FTE) for Elliott Sales de Andrade and
partial support (.2 FTE) for Thomas Caswell.  The effort will be split with
approximately .75 FTE for maintenance, .25 FTE for medium sized enhancements,
and .2 FTE for community and project management.


## Milestones and Deliverables

> List expected milestones and deliverables, and their expected timeline. Be
> specific and include (where possible) any goals for metrics the software
> project(s) are expected to reach upon completion of the grant (maximum of 500
> words)


## Diversity, Equity, and Inclusion (DEI) Statement

> Advancing DEI is a core value for CZI, and we are requesting information on
> your efforts in this area. Describe any efforts the software project(s)
> named in this proposal have undertaken to increase diversity, equity, and
> inclusion with respect to their contributors and audience.  Please see
> examples from applications funded in previous cycles ​(maximum of 250 words)
