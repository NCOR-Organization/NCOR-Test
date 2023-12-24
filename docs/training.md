<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>NCOR Certificate Pathways</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
        }
        body::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-image: url('https://raw.githubusercontent.com/johnbeve/NCOR-Test/main/docs/assets/ncor-pathways.png');
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-size: cover;
            opacity: 0.1; /* Lighten the background */
            z-index: -1;
        }
        header h1 {
            margin: 0;
            color: white;
        }
        main {
            padding: 20px;
        }
        #intro, #open-source {
            background: #f9f9f9;
            padding: 20px;
            text-align: center;
        }
        .siema {
            margin: 20px 0;
            overflow: hidden;
            width: 100%;
        }
        .siema .card {
            min-width: 100%;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            margin: 10px;
            padding: 20px;
            text-align: center;
        }
        .card-container .card {
            background-color: #003366; /* Darker blue */
            color: white;
            padding: 20px;
            margin: 10px;
            border-radius: 10px;
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            border: 2px solid #003366; /* Outer blue border */
        }
        .card-container .card::after {
            content: "";
            position: absolute;
            top: 5px; /* Adjust as needed */
            bottom: 5px; /* Adjust as needed */
            left: 5px; /* Adjust as needed */
            right: 5px; /* Adjust as needed */
            border: 2px solid white; /* Inner white line */
            border-radius: 8px; /* Adjust as needed */
            pointer-events: none;
        }
        .card-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
        }
        .card h3 {
            margin-top: 0;
        }
        button {
            padding: 10px 20px;
            margin: 5px;
            background-color: #007bff;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:focus {
            outline: none;
        }
        .top-image {
            width: 100%;
            display: block;
        }
        @media (max-width: 600px) {
            .card {
                flex-basis: auto;
            }
        }
    </style>
</head>
<body>
    <header>
        <center><h1>NCOR Certificate Pathways</h1></center>
    </header>
    <main>
         <section id="foundational">
            <h2><b>Foundational Certificates</b></h2>
            <p>Explore ontology engineering concepts, technologies, and the semantic web stack that can facilitate their development.</p>
            <div class="card-container">
            <article class="card dropdown">
            <div class="dropdown-toggle">
            <h3>BFO: Basic Formal Ontology Practitioner</h3>
            <p>Learn the basics of BFO classes and relations, applications, and design patterns.</p>
            </div>
            <div class="dropdown-content">
            <center><img src="https://raw.githubusercontent.com/johnbeve/NCOR-Test/main/docs/assets/bfo-practitioner.png" width="25%" height="auto"></center>
                <h4>Overview</h4>
                    <p>The BFO Practitioner Certificate introduces students to the fundamentals of modeling data with the Basic Formal Ontology (BFO), a top-level architecture used by over 500 ontology and knowledge graph projects across the world. Students gain hands-on modeling experiences, working with subject-matter experts on active open-source projects leveraging BFO. Additionally, students will learn the philosophical and practical motivations for the distinctions drawn in BFO. This certificate course covers necessary building blocks for mastering differences and similarities across alternative top-level ontology architectures as well as for leveraging open-source ontologies to model specific domains, such as biomedicine, cyber security, climate change, and immigration, among many others. Throughout the course, students will learn to develop, curate, validate, and implement BFO in support of enterprise solutions.</p>
                <h4>Duration</h4>
                    <p>8 Hours</p>
                <h4>Course Objectives</h4>
                <p>In this course, you will develop competency with the following topics:</p>
                <ul>
                    <li>Top-Level Principles of BFO</li>
                    <li>The BFO Hierarchy</li>
                    <li>Formal Implementations of BFO</li>
                    <li>Translating from Natural Language into BFO</li>
                    <li>Implementing BFO-Conformant Design Patterns</li>
                    <li>Extending BFO by Downward Population</li>
                    <li>Validating Extensions of BFO</li>
                </ul>
                <h4>Intended Audience</h4>
                <p>This course is intended for:</p>
                <ul>
                    <li>Individuals responsible for articulating the benefits of leveraging BFO to others</li>
                    <li>Individuals interested in gaining hands-on training modeling with BFO</li>
                    <li>Knowledge representation, Ontology or Data Architects/Engineers</li>
                    <li>SysOps Administrators</li>
                    <li>Existing users of BFO or extensions of BFO</li>
                </ul>
            </div>
        </article>
                <!-- ONE Course -->
                <article class="card dropdown">
                <div class="dropdown-toggle">
                    <h3>ONE: Ontology Engineer</h3>
                    <p>Participants will gain expertise with standard ontology engineering best practices, tools, and modeling strategies.</p>
                </div>
                <div class="dropdown-content">
                    <center><img src="https://raw.githubusercontent.com/johnbeve/NCOR-Test/main/docs/assets/ontology-engineer.png" width="25%" height="auto"></center>
                    <h4>Overview</h4>
                    <p>The Ontology Engineer Certificate introduces students to the fundamentals of ontology engineering, focused on the creation, updating, maintaining, and validating of ontologies and knowledge graphs in contemporary system architectures. This course provides students hands-on training to master the semantic web stack, equipping students with the competency needed to integrate and curate ontologies effectively. This certificate serves as a stepping stone for certificates covering specialized topics such as optimized information extraction, semantic web devOps best practices, description logic, and cybersecurity related to the semantic web.</p>
                    <h4>Duration</h4>
                    <p>12 Hours</p>
                    <h4>Course Objectives</h4>
                    <p>In this course, you will develop competency with the following topics:</p>
                    <ul>
                        <li>RDF, RDFS, and a zoo of W3C standards</li>
                        <li>OWL2 Full, OWL2 DL Direct Semantics, and OWL Profiles</li>
                        <li>Principles of Version Control using GitHub</li>
                        <li>Open-Source CI/CD tools for ontology development, e.g., Protege, ROBOT, OnTop, GraphDB</li>
                        <li>Extraction and Validation with the Semantic Web Stack, e.g., SPARQL, SHACL</li>
                    </ul>
                    <h4>Intended Audience</h4>
                    <p>This course is intended for:</p>
                    <ul>
                        <li>Individuals using or interested in leveraging semantic web technologies in existing workflows</li>
                        <li>Knowledge representation, Ontology or Data Architects/Engineers</li>
                        <li>Existing users of BFO or extensions of BFO</li>
                        <li>DevOps and SysOps Administrators</li>
                        <li>Software Developers</li>
                    </ul>
                </div>
            </article>
            </div>
        </section>
        <section id="intro">
            <h2><b>Associate Certificates</b></h2>
            <p>Explore ontology engineering concepts, technologies, and the semantic web stack that can facilitate their development.</p>
        </section>
        <section id="courses">
            <div class="card-container">
                <article class="card">
                    <h3>KES: Knowledge Extraction Specialist (Prerequisite: ONE)</h3>
                    <p>Deep-dive into ontology engineering technologies.</p>
                </article>
                <article class="card">
                    <h3>SWD: Semantic Web DevOps Engineer (Prerequisite: ONE)</h3>
                    <p>Deep-dive into ontology engineering technologies.</p>
                </article>
                <article class="card">
                    <h3>TLO: Top-Level Ontology Engineer (Prerequisite: BFO)</h3>
                    <p>Deep-dive into ontology engineering technologies.</p>
                </article>
                <article class="card">
                    <h3>MLO: Mid-Level Ontology Engineer (Prerequisite: BFO)</h3>
                    <p>Deep-dive into ontology engineering technologies.</p>
                </article>
            </div>
        </section>
        <section id="intro">
            <h2><b>Specialist Certificates</b></h2>
            <p>Master specialized ontology engineering topics, such as cyber security and referent-tracking.</p>
        </section>
        <section id="courses">
            <div class="card-container">
                <article class="card">
                    <h3>SWS: Semantic Web Security Specialist (Prerequisites: KES, SWD)</h3>
                    <p>Deep-dive into ontology engineering technologies.</p>
                </article>
                <article class="card">
                    <h3>RTE: Referent Tracking Specialist (Prerequisites: KES, MLO)</h3>
                    <p>Deep-dive into ontology engineering technologies.</p>
                </article>
                <article class="card">
                    <h3>DLS: Description Logic Specialist (Prerequisites: KES, SWD)</h3>
                    <p>Deep-dive into ontology engineering technologies.</p>
                </article>
            </div>
        </section>
        <section id="open-source">
            <h2>Open-Source Courses</h2>
            <p>Explore our collection of open-source training materials to enhance your skills.</p>
            <div class="siema">
                <div class="card">
                    <h3><a href="http://ncorwiki.buffalo.edu/index.php/Applied_Ontology,_Spring_2022">Applied Ontology</a></h3>
                    <p>Dive into applied ontology with open-source tools.</p>
                </div>
                <div class="card">
                    <h3><a href="/index.php/Intelligence_Analysis:_A_Crash_Course">Intelligence Analysis: A Crash Course</a></h3>
                    <p>Learn how to deploy intelligence analytics effectively using open-source software.</p>
                </div>
                <div class="card">
                    <h3><a href="http://ncorwiki.buffalo.edu/index.php/Biomedical_Ontology_2016">Biomedical Ontology</a></h3>
                    <p>Dive into biomedical ontology development with open-source tools.</p>
                </div>
            </div>
            <button class="prev">Previous</button>
            <button class="next">Next</button>
        </section>
    </main>
    <script src="https://cdn.jsdelivr.net/npm/siema@1.5.1/dist/siema.min.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            let mySiema;
            try {
                mySiema = new Siema({loop: true, perPage: 2});
            } catch (e) {
                console.error("Siema failed to initialize: ", e);
            }
            const prevButton = document.querySelector('.prev');
            const nextButton = document.querySelector('.next');
            if (prevButton && nextButton) {
                prevButton.addEventListener('click', () => mySiema.prev());
                nextButton.addEventListener('click', () => mySiema.next());
            }
        });
    </script>
</body>
</html>




        <section id="foundational">
            <h2><b>Foundational Certificates</b></h2>
            <p>Explore ontology engineering concepts, technologies, and the semantic web stack that can facilitate their development.</p>
            <div class="card-container">
                <!-- BFO Course -->
                <article class="card dropdown">
                    <div class="dropdown-toggle">
                        <h3>BFO: Basic Formal Ontology Practitioner</h3>
                        <p>Learn the basics of BFO classes and relations, applications, and design patterns.</p>
                    </div>
                    <div class="dropdown-content">
                        <p>More information about BFO...</p>
                    </div>
                </article>
                <!-- ONE Course -->
                <article class="card dropdown">
                    <div class="dropdown-toggle">
                        <h3>ONE: Ontology Engineer</h3>
                        <p>Deep-dive into ontology engineering technologies.</p>
                    </div>
                    <div class="dropdown-content">
                        <p>More information about ONE...</p>
                    </div>
                </article>
                <!-- Add more foundational courses as needed -->
            </div>
        </section>
        <section id="associate">
            <h2><b>Associate Certificates</b></h2>
            <p>Dive deeper into ontology engineering and semantic technologies.</p>
            <div class="card-container">
                <!-- KES Course -->
                <article class="card dropdown">
                    <div class="dropdown-toggle">
                        <h3>KES: Knowledge Extraction Specialist (Prerequisite: ONE)</h3>
                        <p>Deep-dive into knowledge extraction methodologies and tools.</p>
                    </div>
                    <div class="dropdown-content">
                        <p>More information about KES...</p>
                    </div>
                </article>
                <!-- SWD Course -->
                <article class="card dropdown">
                    <div class="dropdown-toggle">
                        <h3>SWD: Semantic Web DevOps Engineer (Prerequisite: ONE)</h3>
                        <p>Deep-dive into ontology engineering technologies.</p>
                    </div>
                    <div class="dropdown-content">
                        <p>More information about SWD...</p>
                    </div>
                </article>
                <!-- TLO Course -->
                <article class="card dropdown">
                    <div class="dropdown-toggle">
                        <h3>TLO: Top-Level Ontology Engineer (Prerequisite: BFO)</h3>
                        <p>Deep-dive into ontology engineering technologies.</p>
                    </div>
                    <div class="dropdown-content">
                        <p>More information about TLO...</p>
                    </div>
                </article>
                <!-- MLO Course -->
                <article class="card dropdown">
                    <div class="dropdown-toggle">
                        <h3>MLO: Mid-Level Ontology Engineer (Prerequisite: BFO)</h3>
                        <p>Deep-dive into ontology engineering technologies.</p>
                    </div>
                    <div class="dropdown-content">
                        <p>More information about MLO...</p>
                    </div>
                </article>
                <!-- Add more associate courses as needed -->
            </div>
        </section>
        <section id="specialist">
            <h2><b>Specialist Certificates</b></h2>
            <p>Master specialized ontology engineering topics, such as cyber security and referent-tracking.</p>
            <div class="card-container">
                <!-- SWS Course -->
                <article class="card dropdown">
                    <div class="dropdown-toggle">
                        <h3>SWS: Semantic Web Security Specialist (Prerequisites: KES, SWD)</h3>
                        <p>Understand and apply security practices in semantic web applications.</p>
                    </div>
                    <div class="dropdown-content">
                        <p>More information about SWS...</p>
                    </div>
                </article>
                <!-- RTE Course -->
                <article class="card dropdown">
                    <div class="dropdown-toggle">
                        <h3>RTE: Referent Tracking Specialist (Prerequisites: KES, MLO)</h3>
                        <p>Deep-dive into ontology engineering technologies.</p>
                    </div>
                    <div class="dropdown-content">
                        <p>More information about RTE...</p>
                    </div>
                </article>
                <!-- DLS Course -->
                <article class="card dropdown">
                    <div class="dropdown-toggle">
                        <h3>DLS: Description Logic Specialist (Prerequisites: KES, SWD)</h3>
                        <p>Deep-dive into ontology engineering technologies.</p>
                    </div>
                    <div class="dropdown-content">
                        <p>More information about DLS...</p>
                    </div>
                </article>
            </div>
        </section>
  
