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
bio-medical imaging, microscopy, and genomics.
For the past 18 years Matplotlib has been maintained by a vibrant, primarily
volunteer, community.  However given the sheer size of the project and
adoption, we need to supplement the volunteer community with supported full
time maintainers working on the project.  For the past 17 months CZI EOSS
support for developers has had a positive effect on the project by
complementing and enabling, not replacing, volunteer work: we propose to
continue this effort.

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

These tasks underpin the long term health of the library but are ill-suited to
be accomplished with solely volunteer effort.

The primary component of the proposed work is the continued maintenance of the
Matplotlib.  Maintenance covers a wide range of tasks including triaging and
fixing bugs, reviewing Pull Requests, tagging and building releases, and
keeping the continuous integration services running.  These tasks are essential
for the project's health; though each individually is small, they are
frequently time critical and tedious.  It is unfair and impractical to rely
solely on volunteers to accomplish such tasks.


Prior to 2020, with only volunteer effort, we had an ever growing backlog of
Issues and PRs.  Having a large number open Issues and PRs is both discouraging
to new contributors and distracting to the core developers.  Additionally,
there is the risk that good ideas, critical bugs, and beneficial contributions
are being unintentionally overlooked.  In contrast, with CZI support we have
decreased our backlog of open Issues and PRs despite an increase in the number
submitted over the last 15 months.

To ensure the stability of Matplotlib over time we maintain an extensive, but
not exhaustive, test suit of over 8,000 individual tests.  On every PR and on
ever merge to the default branch we automatically run the test suite (and build
the documentation executing almost all of our examples) on a matrix of
supported Python versions and the three major operating systems.  This work is
done in hosted Continuous Integration (CI) services provided to open source
project by the service provides.  While the compute is made available for free,
there is still significant work and specialized knowledge needed to configure
the services.  CI is a key aspect to our quality assurance process, CI passing
is a requirement for merging in normal circumstances, so functioning (and
ideally fast) CI is needed for routine flow of contributions.  If CI it breaks,
it needs to be fixed immediately.  Having supported developers means that we
can prioritize this work to enables the entire community.

Matplotlib is a large, old, and widely used library.  While there are many
incremental improvements that are done by volunteers, some projects are too big
in scope to easily be done by volunteers.  There are medium scale projects
across all aspects of the porject, include fixing long-standing rendering and
performance issues, deep-dive explanatory documentation, homogenizing and
smoothing the API, and new user-facing functionality.  In the previous grant
periods we finishing a 5 year old documentation PR, implemented hi-dpi support
for Tk, and modernizing the parts of the c++ code base.  In these cases the
need was long known (and in the case of the documentation even started!), but
due to lack of dedicated resoures were not completed.




There has been
some recent work, including work supported by the EOSS 1, to improve the layout
of complex multi-Axes Figures.  However, there is an opportunity to
dramatically re-think how we handle the specification and automatic
optimization of the layout.  Currently, the location of the Axes is either
fixed at creation time or users can use two layout methods that are baked into
the Figure that attempt to optimize the layout, to use as much of the space as
possible while avoiding overlaps.  This is not currently implemented in a way
that is easy to extend and add new layout algorithms.  By refactoring the
implementation we can make it possible to implement a variety of algorithms,
even outside of core Matplotlib, including adjusting the Figure size,
re-flowing axes grids a-la flex box, or with an R-stlye view port layout
scheme.


Another set of projects is to improve our support for hatching.
Hatching is an important tool for generating accessible visualizations to
supplement or replace color.  While color can be powerful tool in
visualizations, improper or careless use can lead to visualizations that are
uninterpretable by color-blind individuals or when rendered in black-and-white.
While the underlying Matplotlib backends can support completely arbitrary hatch
patterns, we only expose a limited set (8 primitive patterns with variable
density and their combinations).  Designing an API to allow the user to specify
fully arbitrary hatch patterns, implementing it, and propagating the changes
through all of our backends in a backward-compatible way is a
significant amount of work.


Both of these projects have the possibility of major quality of life
improvements for users for relatively modest investment.  There are many such
medium scale projects in Matplotlib and we will aim to complete 4 such project
each year.  Projects to be pursued with the funding requested here will be
selected in consultation with down-stream biomedical libraries.


The most valuable aspect of the Matplotlib project is the community.  While the
code is what enables our users to get their jobs done, the people who build and
support the code, are the heart of the project.  As with the code, we need to
maintain, support, and grow the community through intentional actions.  This
requires dedicated effort, over long periods of time, beyond what can be
sustained by volunteers alone.


We must ensure that our community is open and welcoming to everyone who wants
to join, with opportunities to contribute in a spectrum of roles as their
interests and skills develop.  However, it is well known that despite our
intentions, open source projects are not diverse organizations, although we do
not have accurate demographics for a majority of our users or contributors.  We
are currently working with Nymphos to conduct a survey of our contributors to
understand the current demography.  Concurrently with this proposal, Matplotlib
is participating in a proposal lead by Melissa Mendonça to create the role of
Contributor Experience Lead (CEL) across Numpy, SciPy, Pandas, and Matplotlib.
Part of the effort on this grant will be to support the CEL working with
Matplotlib and to implement their recommendations.



We propose to continue full support (1 FTE) for Elliott Sales de Andrade and
partial support (.2 FTE) for Thomas Caswell along with travel and equipment
support.  The effort will be split with approximately .75 FTE for maintenance,
.25 FTE for medium sized enhancements, and .2 FTE for community and project
management.  We also propose to fund Code of Conduct incident response training
for the community.


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
