/**
 * Created by Nuno on 02/10/16.
 */

var nmm=nmm||{};
nmm.Main=(function(){
    'use strict';

    function Main(){
        this._init();
    }

    Main.prototype._movieClicked=function(event){
        //TODO params
        var youtubeId=event.target.getAttribute('data-youtube-id');
        this._modalWindow.show(youtubeId);
    };

    Main.prototype._addMovieTilesListeners=function(){
        var i,length=this._movieTiles.length;
        for(i=0;i<length;i++){
            this._movieTiles[i].addEventListener('click',this._movieClicked.bind(this),false);
        }
    };

    Main.prototype._animateTiles=function(){
        var count=0,length=this._movieTiles.length,interval=500;
        this.int=setInterval(function(){
            if(count<length){
                this._movieTiles[count].style.opacity=1;
            }else{
                clearInterval(this.int);
            }
            count++;
        }.bind(this),interval);
    };

    Main.prototype._getMovieTilesReferences=function(){
        this._movieTiles=document.getElementsByClassName('movie-tile');
    };

    Main.prototype._setupModalWindow=function(){
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

nmm.main=new nmm.Main();