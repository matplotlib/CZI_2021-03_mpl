# Proposal purpose

> Limit to one sentence (maximum of 255 characters, including spaces)

> 169 characters

To support the continued maintenance, growth, development, and community
engagement of Matplotlib, the foundational plotting library of the Scientific
Python Ecosystem.


## Round 3 version

To enable Matplotlib to continue as the core plotting library of the Scientific
Python Ecosystem, we will address the maintenance backlog and continue
Matplotlib's evolution to meet the community’s visualization challenges for the
next decade.


# Proposal Summary/Scope of Work (required):

> Provide a short summary of the application (maximum of 500 words)

> currently 475 words

Matplotlib is the foundational data visualization library for the Scientific
Python Ecosystem, with over a million users, including researchers in
bio-medical imaging, microscopy, and genomics.  For the past 18 years
Matplotlib has been maintained by a vibrant, primarily volunteer, community.
However we have grown too big and widely used to continue on solely volunteer
effort.  For the past 15 months (via EOSS Round 1 and 3) we have had supported
developers which has had a huge positive effect on the project.  We propose to
continue this effort.

The primary component of the proposed work is the continued maintenance of the
library.  Maintenance covers a wide range of tasks including triaging bug
reports, fixing bugs, reviewing Pull Requests, tagging and building releases,
and keeping the continuous integration services running.  These tasks are
essential for the project's health; though each individually is small, they are
frequently time critical and tedious.  I is unfair and impractical to rely
solely on volunteers to accomplish such tasks which are best handled by a paid
developer.

In particular, review of new Issues and PRs is a critical task that we were not
able to keep up with prior to 2020 resulting in an ever growing backlog.  There
may be critical bug reports or insightful feature requests among the issues,
while among the PRs there may be useful contributions or bug fixes that would
improve Matplotlib for direct users and downstream packages.  The backlog is
discouraging for new and occasional contributors and distracting for core
developers.

Having maintenance tasks promptly and reliably addressed and reducing the
Issue/PR backlog both drastically improve the contribution experience for
everyone working on the project.  We propose to devote three quarters of a
developer's time to continue handling these tasks.

In addition to on-going and routine maintenance, there are substantial, but
incremental, enhancement to Matplotlib that require long blocks of dedicated
work to implement.  Examples of this work include fixing long-standing
rendering and performance issues, deep-dive explanatory documentation,
homogenizing and smoothing the API, and new user-facing functionality.  Without
funding, this type of project can drag out for months to years or stall
altogether.  We propose to complete 4 such medium-sized self-contained projects
per year with about 20% of an FTE.  The exact projects will be selected in
consultation with down-stream biomedical libraries.


Matplotlib is a community-driven project with individuals participating at all
levels of engagement, from users who need to be notified when a new release is
available to developers who are co-creating the library and everything in
between.  The supported developers must complement and enable, not replace,
crucial volunteer work.  It is critical that we foster our community and there
are paths for people to change their role within community.  We propose
dedicating a 20% FTE to community maintenance, including governance, outreach,
communications, and moderation.




# Landscape analysis

> Briefly describe the other software tools (either proprietary or open source)
> that the audience for this proposal is primarily using. How do the software
> projects in this proposal compare to these other tools in terms of user base
> size, usage, and maturity? How do existing tools and the project(s) in this
> proposal interact? (maximum of 250 words)

> currently 136 words (lifted from cycle 3 text and lightly edited)

Matplotlib is the most widely used and de-facto standard visualization library
in Python (over 1M monthly users) and is a mature library (18+ years old) with
over 1,250 individual code contributors.  In addition to being directly used by
scientists, it is a core dependency of libraries and applications that
implement domain-specific visualizations. To aid users in discovering these
extensions we have been assigned a Trove classifier on PyPI [1].

Given the centrality of visualization to data analysis across all domains, no
single tool can satisfy all needs.  There are a range of tools not built on
Matplotlib (see https://pyviz.org/tools.html for a long but not exhaustive
list) that target use cases that Matplotlib is not well suited for.  A

[1] https://pypi.org/search/?q=&o=&c=Framework+%3A%3A+Matplotlib

# Value to Biomedical Users:

> Briefly described the expected value the proposed scope of work will deliver
> to the biomedical research community (maximum of 250 words)

> 87 Words

Visualization is fundamental to science across all domains, including
biomedical, and Matplotlib is the foundational plotting library in the
scientific Python Ecosystem.  As a general-purpose plotting library Matplotlib
is used to build domain specific visualization by researches across the
biomedical research community, both directly and indirectly via tools that
implement domain-specific visualizations.  This tools including CZI funded
projects scikit-learn, CellProfiler, scanpy, starfish, nipy, networkx,
MNE-python, DeepCutLab, pandas, xarary, and scikit-image.  Supporting the
maintenance of Matplotlib will support researchers across the biomedical complex.
