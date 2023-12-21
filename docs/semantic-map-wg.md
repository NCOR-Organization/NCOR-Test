<style>
body {
  position: relative;
  height: 100vh; 
  margin: 0;
  background: transparent;
}

body::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url('https://raw.githubusercontent.com/johnbeve/NCOR-Test/main/docs/assets/NCOR_image.png');
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
  opacity: 0.1;
  z-index: -1;
}
</style>

The PROV-O to BFO working group has the aim of mapping the Provenance Ontology into the BFO environment. The group of ontologists and developers meets weekly in order to discuss possible translations between the two frameworks and create a standardized vocabulary to structure Provenance information.
