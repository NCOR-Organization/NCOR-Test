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
        header {
            background: #232f3e;
            color: white;
            padding: 1rem;
            text-align: center;
        }
        header h1 {
            margin: 0;
        }
        main {
            padding: 20px;
        }
        #intro, #intro2, #intro3, #open-source {
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
        <img src="assets/ncor-pathways.png" alt="NCOR Pathways" class="top-image">
        <h1>NCOR Certificate Pathways</h1>
    </header>
    <main>
        <section id="intro">
            <h2>Foundational Certificates</h2>
            <p>Explore ontology engineering concepts, technologies, and the semantic web stack that can facilitate their development.</p>
        </section>
        <section id="courses">
            <div class="card-container">
                <article class="card">
                    <h3>BFO: Basic Formal Ontology Practitioner</h3>
                    <p>Learn the basics of BFO classes and relations, applications, and design patterns.</p>
                </article>
                <article class="card">
                    <h3>ONE: Ontology Engineer</h3>
                    <p>Deep-dive into ontology engineering technologies.</p>
                </article>
            </div>
        </section>
        <section id="intro2">
            <h2>Associate Certificates</h2>
            <p>Explore ontology engineering concepts, technologies, and the semantic web stack that can facilitate their development.</p>
        </section>
        <section id="courses2">
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
        <section id="intro3">
            <h2>Specialist Certificates</h2>
            <p>Master specialized ontology engineering topics, such as cyber security and referent-tracking.</p>
        </section>
        <section id="courses3">
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
                    <h3><a href="http://ncorwiki.buffalo.edu/index.php/Biomedical_Ontology_2016">Biomedical Ontology</a>/h3>
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
                mySiema = new Siema();
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
