/*
 * Serves the start page animations of cards within the jumbotron_start
*/
function start_page_jumbo_animation () {
  $(".jumbo-story-text-1").typed({
    strings: ["As a Product Owner, I'd like to use FRNKN so that I can write awesome user stories for my dev team."],
    typeSpeed: 0,
    showCursor: false,
    callback: function() {
      $(".jumbo-card-1").addClass('animated bounceOutDown').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend',
         function(){
           $(".jumbo-card-1").addClass('hidden-xs-up');
           $(".jumbo-card-2").removeClass('hidden-xs-up');
           $(".jumbo-story-text-2").typed({
             strings: ["As a Product Manager, I'd like to manage acceptance criteria, non functional requirements and wireframes with FRNKN, so that I create the best software specs ever."],
             typeSpeed: 0,
             showCursor: false,
             callback: function(){
               $(".jumbo-card-2").addClass('animated bounceOutDown').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend',
                  function(){
                    $(".jumbo-card-2").addClass('hidden-xs-up');
                    $(".jumbo-card-3").removeClass('hidden-xs-up');
                    $(".jumbo-story-text-3").typed({
                      strings: ["As a Product Manager, I'd like to print my stories with FRNKNs awesome print functionalities, so that I can put my stories on my physical whiteboard."],
                      typeSpeed: 0,
                      showCursor: false,
                      callback: function(){
                        $(".jumbo-card-3").addClass('animated bounceOutDown').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend',
                           function(){
                             $(".jumbo-card-3").addClass('hidden-xs-up');
                             $(".jumbo-card-4").removeClass('hidden-xs-up');
                             $(".jumbo-story-text-4").typed({
                               strings: ["As a new FRNKN customer, I'd like to sign up for my early bird backlog asap, so that I experience the awesomeness of FRNKN!"],
                               typeSpeed: 0,
                               showCursor: false,
                               callback: function(){
                                 $("#mc_embed_signup").removeClass('hidden-xs-up');
                                 $("#mc_embed_signup").addClass('animated zoomIn');
                               }
                             }
                          );
                        }
                      );
                    }
                  });
                 }
               );
             }
           });
         }
       );
    },
  });
}

/**
* Defining the main app
**/
function App(){};


App.prototype = {
  constructor: App,
  sayHello:function(){
    console.log("HELLO FRNKN APP");
  },
  dosth:function(){
    console.log("Do Sth");
  }
}
