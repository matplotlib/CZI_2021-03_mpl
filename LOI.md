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

> currenly 511 words

Matplotlib is the foundational data visualization library for the Scientific
Python Ecosystem for creating static, animated, and
interactive visualizations.   Matplotlib has over a million users,
including researchers in bio-medical imaging, microscopy, and genomics.
Scientists use Matplotlib both both directly and indirectly via CZI funded
projects such as scikit-learn, CellProfiler, scanpy, starfish,
nipy, MNE-python, and scikit-image.
For the past 18 years Matplotlib has been maintained by a vibrant, primarily
volunteer, community.  However, we have grown to the point where we need
supported developers with the time to organize, plan, and make decisions.

The continued maintenance of the library is the primary component of the
proposed work.  Maintenance covers a wide range of tasks including triaging bug
reports, fixing bugs, reviewing Pull Requests, tagging releases, and keeping
the continuous integration services running.  Issues and PRs are submitted
faster than our volunteers can review them.  There may be critical bug reports
or insightful feature requests among the former, while among the latter are
useful contributions or bug fixes that would improve Matplotlib for direct
users and downstream packages. The backlog is discouraging for new and
occasional contributors and distracting for core developers.


These tasks are essential for the project's health; though each individually is
small, they are frequently time critical and tedious.  They are best handled by
a paid developer because it is unfair and impractical to rely solely on
volunteers to accomplish such tasks.  In addition, having these tasks promptly
and reliably addressed improves the contribution experience for everyone
working on the project.  We propose to devote three quarters of a developer's
time to handling these tasks.

In addition to routine and on-going maintenance tasks, there are substantial,
but incremental, improvements that require long blocks of dedicated work to
implement.  Examples of this work include fixing long-standing rendering and
performance issues, deep-dive documentation, homogenizing and smoothing the
API, and new user-facing functionality.  Without funding, this type of project
can drag out for months or stall altogether.  We propose to complete 4 such
medium-sized self-contained projects per year with about 20% of an FTE.  These
projects will be selected in consultation with down-stream bio-libraries.


Matplotlib is a community-driven project with individuals at at all levels of
engagement, from community members whom we need to primarily convey information
to to developers who are co-creating the library.  We need to ensure that there
is paths for people to join and change their role within community.
We run several open-to-the-public spaces that require moderation.  We need to
facilitate discussions around proposed enhancements, features, and API changes.
We propose dedicating a 20% FTE to community maintenance, including governance,
outreach, communications, and moderation.


The requested support is intended to complement, not replace, crucial volunteer
work.  For the past 15 months (starting Jan 2020), funding from CZI has allowed
us to have supported developers working on Matplotlib which has been immensely
valuable.  This has the direct effect of improving the library for our users
and improving the experience of our contributors and community.




# Landscape analysis

> Briefly describe the other software tools (either proprietary or open source)
> that the audience for this proposal is primarily using. How do the software
> projects in this proposal compare to these other tools in terms of user base
> size, usage, and maturity? How do existing tools and the project(s) in this
> proposal interact? (maximum of 250 words)

> currently 174 words (lifted from cycle 3 text)

Matplotlib is the most widely used and de-facto standard visualization library
in Python (over 1M monthly users) and is a mature library (18+ years old) with
over 1,250 individual code contributors.  In addition to being directly used by
scientists, it is a core dependency of libraries and applications that
implement domain-specific visualizations, including CZI funded projects such as
scikit-learn, CellProfiler, scanpy, starfish, nipy, MNE-python, and
scikit-image. To aid users in discovering these extensions we have recently
been assigned a Trove classifier on PyPI [1] (which we applied for due to a
conversation at the first CZI EOSS summit).

Given the centrality of visualization to data analysis across all domains, no
single tool can satisfy all needs.  There are a range of tools not built on
Matplotlib (see https://pyviz.org/tools.html for a long but not exhaustive
list) that target use cases that Matplotlib is not well suited for.  A side
effect of our work will be to increase the interoperability of these tools,
letting users use the right tool (or mix of tools) for the job.

[1] https://pypi.org/search/?q=&o=&c=Framework+%3A%3A+Matplotlib

# Value to Biomedical Users:

> Briefly described the expected value the proposed scope of work will deliver
> to the biomedical research community (maximum of 250 words)

Visualization to data analysis across all domains including biomedical.
Matplotlib is directly used by scientists, it is central to many libraries and
applications that implement domain-specific visualizations, including CZI
funded projects such as scikit-learn, CellProfiler, scanpy, starfish, nipy,
mne-python and scikit-image.
