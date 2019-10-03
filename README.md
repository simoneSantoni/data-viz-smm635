Module Overview
===============

In the digital era, we are bombarded by humongous streams of
information. Sometimes, these 'inputs' are not interesting enough to
breach the defensive barriers that protect our attention―hence, we
simply decide to pass over. Other times, what we are exposed to seems
valuable but we do not see any neat, meaningful pattern in it (that's
the bottom line as it comes to crunch massive datasets!!). According to
the popular idiom *"one picture is worth a thousand words"*, all what
messengers and audiences need to 'click' is―often-times―just a
simple, effective visualization.

This module is a journey into the art and science of creating memorable
charts, which grab the attention of the audience and successfully convey
insights and narratives. Pleasant journeys require good companions:
'infographic'―i.e., the field that investigates the representation of
information, data, and knowledge―will offer the theoretical platform
for the module; Python will make things happen (at least on our screen).
Consistently with the teaching philosophy of the module leader, each
individual lecture integrates 'theory' and 'practice'.


Materials & Readings
====================

Mandatory materials/readings will be circulated via Moodle in advance
(Monday). For this module you are not required to purchase any expensive
book, whereas it is essential you carefully go through:

-   lecture notes (to be uploaded onto
    Moodle/[Github](https://github.com/simoneSantoni/data-viz-smm635) weekly);

-   Python scripts/Jupyter notebooks (to be uploaded onto
    Moodle/[Github](https://github.com/simoneSantoni/data-viz-smm635)
    weekly);

-   journal articles (to be uploaded onto
    Moodle/[Github](https://github.com/simoneSantoni/data-viz-smm635)
    weekly).

Discretionary readings/materials students may want to reference to are:

-   [Knowledge is
    Beautiful](https://informationisbeautiful.net/2014/knowledge-is-beautiful/)

-   [The Functional
    Art](http://www.thefunctionalart.com/p/about-book.html)

-   [The Information Capital](http://theinformationcapital.com/)

-   [The Visual Display of Quantitative
    Information](https://www.amazon.co.uk/Visual-Display-Quantitative-Information/dp/0961392142/ref=sr_1_3?ie=UTF8&qid=1537986137&sr=8-3&keywords=edward+tufte).


Learning Objectives and Assessment
==================================

At the end of the module, students should be able to:

-   generate and evaluate visual forms for appropriateness, context, and
    meaning;

-   design and execute statical charts with a particular emphasis on
    massive datasets;

-   design and execute complex visualizations involving timeliness and
    geospatial attributes;

-   design and execute interactive visualizations;

-   leverage the visualization capabilities of the Python libraries
    [Matplotlib](https://matplotlib.org/) and
    [Bokeh](https://bokeh.pydata.org/).

As per the module specification, students will be assessed on the basis
of coursework submissions, which all are the outcome of group-level
efforts (yes, you understand correctly, for this module there is no
final examination and you are not supposed to deliver any assignment on
your own). Specifically, there are two pieces of coursework, namely a
'mid-term project' (MTP), and a 'final course project' (FCP), which
contribute to the final mark (FM) as follows:

FM = 0.25 X MTP + 0.75 X FCP

For the **mid-term project**, students are required to solve a complex
visualization problem. This year, the project will focus on the topic of
'popularity' in markets (details will be available by week 3, when the
project will be released). Submissions will be assessed on a
0 - 100% scale. The Groups who fail can resubmit a revised version
of the project; if the revision is sufficient, students receive a 50%
mark. The deadline for the project is November 11 (week 6). Selected
groups will be invite to present the outcome of their work to fellow
students in week 6.

With the **final course project** (due by week 10, see Table 1), groups
make their hands 'dirty' as they help a real-world client to face some
data visualization challenges. Details about the client and the
challenge will be available in week 8. Final course projects will be
evaluated on a rolling-based window and should be submitted by December
20.

Both types of assessment will be evaluated along four criteria: i)
appropriate use of notions and frameworks discussed in class; ii)
effectiveness of the proposed answer or solution; iii)
originality/creativity of the proposed answer or solution; iv)
organization an clarity of submitted materials. All criteria carry-out
equal weight in terms of mark.

**Problem sets** will be launched weekly. Students may want to deal
these problem sets and present their solution to the class. One student
per session will be selected on the basis of the novelty and
effectiveness of the proposed solution. One bonus point
(+1 FM) will be assigned.


Schedule of the Module
======================

| Week | Topic                                                                          |
|:----:|--------------------------------------------------------------------------------|
| 1    | Introduction to the module                                                     |
| 2    | Elements of infographic                                                        |
|      | - taste, aesthetics, and perceptions                                           |
|      | - visual forms                                                                 |
|      | - colors                                                                       |
|      | - exemplars of visualization                                                   |
|      | Exploratory statistical charts                                                 |
|      | - frequencies                                                                  |
|      | - univariate distributions                                                     |
|      | - bivariate distributions                                                      |
|      | - 3D distributions                                                             |
|      | Laboratory sessions (Matplotlib)                                               |
| 3    | Time-dependent data                                                            |
|      | - timelines                                                                    |
|      | - sequences of events                                                          |
|      | - narrative                                                                    |
|      | Laboratory sessions (Matplotlib)                                               |
| 4    | Visualizing statical estimates and fits                                        |
|      | - uncertainty in estimates                                                     |
|      | - plotting causal effects estimated via regression                             |
|      | - comparing causal effects across groups                                       |
|      | Laboratory sessions (Matplotlib)                                               |
| 5    | Geospatial maps, part I                                                        |
|      | Laboratory sessions (Fiona + Pyshp + Rasterio + Pyproj + Shapeley + Geopandas) |
| 6    | Mid-term project in class-presentations                                        |
| 7    | Geospatial maps, part II                                                       |
|      | Laboratory sessions (Fiona + Pyshp + Rasterio + Pyproj + Shapeley + Geopandas) |
| 8    | Final course project release                                                   |
| 9    | Interactive visualizations for the web, part I                                 |
|      | Laboratory sessions (Bokeh)                                                    |
| 10   | Interactive visualizations for the web, part I                                 |
|      | Laboratory sessions (Bokeh)                                                    |


Prerequisites
=============

The SMM692 ― Python Pre-Course module defines the knowledge students
should possess in order to proficiently attend to SMM635 ― Data
Visualization.


Software requirements
=====================

For this module you are supposed to run Python 3.7 on your machine. Now,
how to get Python work on your machine? There are several ways to do
that. A fast, smooth alternative is to install
[Anaconda](https://www.anaconda.com/what-is-anaconda/), an open source
distribution of Python that includes: i) 250+ popular data science
packages; ii) the [conda](https://conda.io/docs/index.html) package,
which makes quick and easy to install, run, and upgrade complex data
science and machine learning environments.

Here is the workflow:

1.  Use your preferred browser to open the link pointing to the
    [Anaconda repository](http://www.numpy.org/);

2.  Select the installer the which suits your machine (32- or 64-bit)
    and operating system (Win, Mac OS, Linux). Mac users may want to
    download the graphical installer rather than the command-line
    installer (students may feel less comfortable with);

3.  Retrieve the installer (perhaps in your download folder);

4.  Run the installer;

5.  Log-out from your current session (it does not matter if you use
    Win, Mac OS or Linux);

6.  Log-in into a new session;

7.  Run 'Anaconda Navigator'―namely, a convenient place to launch the
    IPython shell or other user-interfaces to interact with IPython.

On top of Anaconda/Python, students should install the modules
[Matplotlib](https://networkx.github.io/),
[Bokeh](https://bokeh.pydata.org/en/latest/),
[Fiona](http://toblerity.org/fiona/manual.html),
[Pyshp](https://glenbambrick.com/tag/pyshp/),
[Rasterio](https://rasterio.readthedocs.io/en/latest/),
[Shapely](https://shapely.readthedocs.io/en/stable/manual.html) (I
recommend to do that using Conda).
