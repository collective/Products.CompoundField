CompoundField
=============

This Product includes CompoundField and ArrayField. Both are fields for use 
within Archetypes Products. 
 
CompoundField 
    field that itself consists of several sub-fields defined in 
    an own Schema. 

ArrayField 
    field containing one field severals times.

It also provide basic widgets for both fields.
 
EnhancedArrayWidget is an improved ArrayWidget, using Javascript to expand and shrink
the array client side. 

Dependencies

  - Zope 2.9.5+, Zope 2.10.x

  - Plone 2.5.+ or 3.0.+

  - Archetypes 1.4.+ or 1.5.+


 Documentation

  Please have a look at the doc-tests in docs directory and the model
  in model the directory.


 Authors

  Phil Auersperg -- idea, concept, model, code, tests, ArchGenXML integration;
                    phil@bluedynamics.com

  Jens Klein -- idea, concept; jens@bluedynamics.com 
  
  Sune Broendum Woeller -- EnhancedArrayWidget; sune[AT]woeller.dk

  Eric Brehault -- validator; <ebrehault@gmail.com>

Copyright

  eduplone Open Source Business Network EEIG, Austria, 2005-2006
  BlueDynamics Alliance, Austria, 2007-2008

  This code was initially created for the ZUCCARO project. 
  ZUCCARO (Zope-based Universally Configurable Classes for Academic 
  Research Online) is a database framework for the Humanities developed 
  by the Bibliotheca Hertziana, Max Planck Institute for Art History
  For further information: "zuccaro.biblhertz.it":http://zuccaro.biblhertz.it/ 


Licence

 **German Free Software License (D-FSL)** see "www.d-fsl.org":http://www.d-fsl.org

 This license conforms to the GNU General Public License and is 
 adapted to the particular requirements of German and European law. 
 It was inspired by the 'Berlin Declaration on Open Access to 
 Knowledge in the Sciences and Humanities' which was signed by the 
 'Max Planck Society for the Advancement of Science'.


Todo

  - Improve UI of Widgets (contributions are welcome!)
  - Handle different COMPOUND_FIELD_SEPERATORs in EnhancedArrayWidget 
    (is it needed?)
  - Fix bug with Arrays of Arrays (Do we want to support this at all?)
  

