# Proposal purpose

> Limit to one sentence (maximum of 255 characters, including spaces)

> 244 characters

To enable Matplotlib to continue as the core plotting library of the Scientific
Python Ecosystem, we will address the maintenance backlog and continue
Matplotlib's evolution to meet the community’s visualization challenges for the
next decade.

# Proposal Summary/Scope of Work (required):

> Provide a short summary of the application (maximum of 500 words)

Matplotlib is the foundational data visualization library for the Scientific
Python Ecosystem, with over a million users, including researchers in
bio-medical imaging, microscopy, and genomics. It has been actively developed
and maintained by a vibrant, primarily volunteer, community for the past 18
years.  In the past 15 months, with supported developers, we reduced our
backlog of open Issues and Pull Requests. This is a marked change from the
previous few years, when both were steadily increasing with only volunteer
effort. We propose to support 0.9 FTE of effort to continue maintenance,
mid-sized enhancements, and user support.  This has the direct effect of
improving the library for our users and improving the experience of our
contributors and community.

We also propose committing approximately a quarter of FTE to community
maintenance, inculding goverance.



# Landscape analysis

> Briefly describe the other software tools (either proprietary or open source)
> that the audience for this proposal is primarily using. How do the software
> projects in this proposal compare to these other tools in terms of user base
> size, usage, and maturity? How do existing tools and the project(s) in this
> proposal interact? (maximum of 250 words)

> currently 174 words (lifted from cycle 3 text)

Matplotlib is the most widely used and de-facto standard visualization library
in Python (over 1M monthly users) and is a mature library (17+ years old) with
over 1,250 individual code contributors.  In addition to being directly used by
scientists, it is central to many libraries and applications that implement
domain-specific visualizations, including CZI funded projects such as
scikit-learn, CellProfiler, scanpy, starfish, nipy, and scikit-image. To aid
users in discovering these extensions we have recently been assigned a Trove
classifier on PyPI [1] (which we applied for due to a conversation at the first
CZI EOSS summit).

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
