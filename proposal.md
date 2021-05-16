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

> A short summary of the application ​(maximum of 500 words) (auto-filled from
> LOI; update if needed)

> The initial call trimmed this to 250 words, and then updated it back to 500
> this is a (very) cut down version I got to.  Not sure if we want to stay with
> the shorter version or stick with the original version

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


> original
> 463 words

Matplotlib is the foundational data visualization library for the Scientific
Python Ecosystem, with over a million users, including researchers in
bio-medical imaging, microscopy, and genomics.  For the past 18 years
Matplotlib has been maintained by a vibrant, primarily volunteer, community.
However we have grown too big and widely used to continue on solely volunteer
effort.  For the past 15 months CZI EOSS support for developers has had a
positive effect on the project by complementing and enabling, not replacing,
volunteer work.  We propose to continue this effort.



The primary component of the proposed work is the continued maintenance of the
library.  Maintenance covers a wide range of tasks including triaging and
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


In addition to on-going and routine maintenance, there are substantial, but
incremental, enhancement to Matplotlib that require long blocks of dedicated
effort to implement.  Without funding, this type of project can drag out for
months to years or stall altogether.  Examples include fixing long-standing
rendering and performance issues, deep-dive explanatory documentation,
homogenizing and smoothing the API, and new user-facing functionality.
Projects to be pursued with the funding requested here will be selected in
consultation with down-stream biomedical libraries.



Finally, supported developers improve the management of the project.  We now
have the time and bandwidth to make strategic decisions about the direction of
the project to ensure the long term health and viability of Matplotlib.  An
important part of project management is community management: fostering,
diversifying, and growing our community.  This requires dedicated effort, over
long periods of time, beyond what can be sustained by volunteers alone.  We
must ensure that our community is open and welcoming to everyone who wants to
join, with opportunities to contribute in a spectrum of roles as their
interests and skills develop.


We propose to continue full support (1 FTE) for Elliott Sales de Andrade and
partial support (.2 FTE) for Thomas Caswell.  The effort will be split with
approximately .75 FTE for maintenance, .25 FTE for medium sized enhancements,
and .2 FTE for community and project management. We also propose to fund Code
of Conduct incident response training for the community.



## work plan

> A description of the proposed work the applicants are requesting funding for,
> including resources the applicants will provide that are not part of the
> requested funding. For software development-related work (e.g., engineering,
> product design, user research), specify how the work fits into the existing
> software project roadmap.  For community outreach related activities (e.g.,
> sprints, training), specify how these activities will be organized, the
> target audience, and expected outcomes (maximum of 750 words)

> 982 words

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
Issues and PRs.  A large backlog of open Issues and PRs is discouraging to new
contributors and distracting to the core developers.  It is almost certain that
good ideas, critical bugs, and beneficial contributions are being
unintentionally overlooked.  In contrast, with CZI support we have decreased
our backlog of open Issues and PRs despite an increase in the number opened
over the last 15 months.

To ensure the stability of Matplotlib over time we maintain an extensive test
suite.  When changes are proposed we run the full test suite and build the
documentation on all of the supported Python versions and major operating
systems via hosted Continuous Integration (CI) services.  This CI is a key
aspect to our quality assurance process: CI passing is a requirement for
merging any changes to the default branch and is needed for the routine flow of
contributions.  While the service provides offer free resources to open source
projects, significant work and specialized knowledge is needed to configure and
maintain them.  Having supported developers who can prioritize this work
enables the entire community.

There are innumerable incremental improvements to Matplotlib that can readily
be done by volunteers, however some projects are too big in scope to easily be
done by volunteers.  There are medium scale projects across all aspects of the
project from fixing long-standing bugs, improving the performance,
documentation tasks, or implementing major new features.  Examples of this work
from the the previous grant periods include: finishing a 5 year old
documentation PR, implementing hi-dpi support for Tk, and modernizing the parts
of the c++ code base.  The common theme of these projects is the need for
long blocks of dedicated time to devoted to the project.

Recent work, including work supported by the EOSS 1, has drastically improved
the layout of complex multi-Axes Figures.  This work has shown that there is an
opportunity to dramatically re-think how we handle the specification and
automatic optimization of the layout.  Currently there are two layout
algorithms built into Matplotlib and no way to inject additional algorithms
without modifying the core library.  We propose refactor this to allow the
layout algorithms to be injected by defining a consistent API to adjust the
layout of a Figure.  This will enable implementing a variety of algorithms,
even outside of core Matplotlib, including adjusting the Figure size,
re-flowing axes grids a-la flex box, or with an R-stlye view port layout
scheme.

Another possible project is to improve our support for hatching.  Hatching,
filling an area with a texture pattern, is an important tool for generating
accessible visualizations by supplementing or replacing color.  Currently
Matplotlib only exposes a limited set of patterns (8 primitive patterns which
can be combined with varying density) to the user.  However, the underlying
code can support arbitrary patterns!  We propose to extend the existing API to
expose the full set of capabilities to the user.

These projects are illustrative of medium scale projects that existing within
Matplotlib will drastically for users for relatively modest investment.  These
projects, which include aspects of API design, extensive documentation, and
implementation effort, are far more successful with dedicated effort rather
than volunteer effort alone.

The most valuable aspect of the Matplotlib project is the community.  While the
code is what enables our users to get their jobs done, the people who build and
support the code, are the heart of the project.  As with the code, we need to
maintain, support, and grow the community through intentional actions.  This
requires dedicated effort, over long periods of time, beyond what can be
sustained by volunteers alone.  We must ensure that our community is open and
welcoming to everyone who wants to join, with opportunities to contribute in a
spectrum of roles as their interests and skills develop.

Although we do not have accurate demographics for our community, we believe
that the diversity of our contributors does not match the diversity of our
users.  To quantify and understand how to address this imbalance and increase
the over all diversity we are collaborating with other efforts. First, NumFOCUS
is currently working to quantify the demographics of our projects and
understand the barriers to entry for under-represented groups.  We anticipate
that the initial results of that work will be available near the start of the
funding period of this proposal.  Further, Matplotlib is supporting a proposal
lead by Melissa Mendonça to create and fund a Contributor Experience Lead (CEL)
role across Numpy, SciPy, Pandas, and Matplotlib which would run concurrently
with this proposal.  While we do not yet know what the recommendations of these
efforts will be, we commit to implementing them in the Matplotlib community.

We propose to continue full support (1 FTE) for Elliott Sales de Andre and
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

> 164 words

Quantitatively evaluating maintenance work can be tricky---some Issues or PRs
take minutes to review while others can take days to weeks of effort---but we
believe that there is value at looking at the throughput of issues and PRs
supported by the grant.  The total number of open issues and PRs is dependent
on both how many come in and the amount of work done by volunteers.  We will
aim to hit the following metrics:

- Initial response to all issues / new PRs within a week
- Resolve majority of new issues / PRs within 1 month
- Review and resolve 100 issues / quarter
- Reduce and merge or close 100 PRs / quarter
- 8 mid-sized new features (4 per year)
- Feature releases every 6 months, 2-3 patch releases between feature releases

As mentioned above, Matplotlib is involved in on-going and proposed work on
improving diversity in our community.  We will implement the recommendations of
those efforts and, if funded, support the Matplotlib Contributor Experience
Lead.



## Diversity, Equity, and Inclusion (DEI) Statement

> Advancing DEI is a core value for CZI, and we are requesting information on
> your efforts in this area. Describe any efforts the software project(s)
> named in this proposal have undertaken to increase diversity, equity, and
> inclusion with respect to their contributors and audience.  Please see
> examples from applications funded in previous cycles ​(maximum of 250 words)


Matplotlib is committed to being an open and welcoming project. We believe that
transparency and explicitness of process and in communication are key to
building an inclusive, equitable, and diverse project. In our effort to be
welcoming, we have worked at being more explicit about our norms and values and
how the project operates. To this end, we have put major effort into
documenting our governance and defining leadership roles, and clarifying
specific expectations for new code and community contributors.  We have started
two initiatives to lower the barrier of entry for individuals to get
involved in developing Matplotlib:: an triage role in the project and an
"incubator" channel on our gitter.  It is critical that all contributors,
independent of experience level both in general and with the project, feel safe
to make mistakes and learn in our community.  We strive to embody these values
in our interactions on github, our mailing list and community discussion forum
(discourse), and in our social media.  We hope that these practices will
empower and encourage people who have diverse identities to participate in
Matplotlib.
