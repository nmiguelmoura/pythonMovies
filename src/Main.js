/**
 * Created by Nuno on 02/10/16.
 */

var nmm=nmm||{};
nmm.Main=(function(){
    'use strict';

    //class that initiates functionality and animation

    function Main(){
        this._init();
    }

    Main.prototype._movieClicked=function(event){
        //get data-youtube-id attribute form div
        var youtubeId=event.target.getAttribute('data-youtube-id'),
            overview=event.target.getAttribute('data-overview');

        //show modal window
        this._modalWindow.show(youtubeId,overview);
    };

    Main.prototype._addMovieTilesListeners=function(){
        var i,length=this._movieTiles.length;
        for(i=0;i<length;i++){
            this._movieTiles[i].addEventListener('click',this._movieClicked.bind(this),false);
        }
    };

    Main.prototype._animateTiles=function(){
        //animates the opacity of movie_tiles
        //shows one each half-second
        var count=0,length=this._movieTiles.length,interval=500;
        this.int=setInterval(function(){
            if(count<length){
                //if some are not showing
                this._movieTiles[count].style.opacity=1;
            }else{
                //if all are animated
                clearInterval(this.int);
            }
            count++;
        }.bind(this),interval);
    };

    Main.prototype._getMovieTilesReferences=function(){
        //get the DOM references to the class movie-tile
        this._movieTiles=document.getElementsByClassName('movie-tile');
    };

    Main.prototype._setupModalWindow=function(){
        //launchs modal window that shows trailer
        this._modalWindow=new nmm.ModalWindow();
    };

    Main.prototype._init=function(){
        this._setupModalWindow();
        this._getMovieTilesReferences();
        this._animateTiles();
        this._addMovieTilesListeners();
    };

    return Main;
})();

//instanciate class Main
nmm.main=new nmm.Main();