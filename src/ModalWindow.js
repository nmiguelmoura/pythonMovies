/**
 * Created by Nuno on 02/10/16.
 */

var nmm=nmm||{};
nmm.ModalWindow=(function(){
    'use strict';

    function ModalWindow(){
        //modal window exists
        this.exists=false;

        //is iFrame created
        this._iFrameCreated=false;
        this._init();
    }

    ModalWindow.prototype._closeWindow=function(){
        //hide modal window
        this._modalTrailer.style.display='none';
        this._closeBtn.removeEventListener('click',this._closeBind,false);

        //destroy src from iFrame
        this._iFrame.src='';
    };

    ModalWindow.prototype._createiFrame=function(){
        //create iFrame document
        this._iFrame=document.createElement('iFrame');

        //set iFrame attribute
        this._iFrame.setAttribute('type','text-html');

        //append iframe in video div
        this._videoDiv.appendChild(this._iFrame);
        this._iFrameCreated=true;
    };

    ModalWindow.prototype._playMovie=function(youtubeId){
        if(!this._iFrameCreated){
            //if iframe was not created
            this._createiFrame();
        }

        //change src of iframe
        this._iFrame.src='https://www.youtube.com/embed/'+youtubeId+'?autoplay=1&html5=1';
    };

    ModalWindow.prototype.show=function(movieUrl){
        //show modal window if exists
        if(this.exists){
            //show modal window
            this._modalTrailer.style.display='block';

            //bind for click close btn function
            this._closeBind=this._closeWindow.bind(this);
            this._closeBtn.addEventListener('click',this._closeBind,false);

            //show movie
            this._playMovie(movieUrl);
        }
    };

    ModalWindow.prototype._getWindowReferences=function(){
        //get DOM references for modal window and inside div elements
        this._modalTrailer=document.getElementsByClassName('modal-window-trailer')[0];

        //get references to closeBtn and video div only if modaltrailer exists
        if(this._modalTrailer){
            this.exists=true;
            this._closeBtn=this._modalTrailer.getElementsByClassName('close-btn')[0];
            this._videoDiv=this._modalTrailer.getElementsByClassName('video')[0];
        }
    };

    ModalWindow.prototype._init=function(){
        this._getWindowReferences();
    };

    return ModalWindow;
})();