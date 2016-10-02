/**
 * Created by Nuno on 02/10/16.
 */

var nmm=nmm||{};
nmm.ModalWindow=(function(){
    'use strict';

    function ModalWindow(){
        this.exists=false;
        this._iFrameCreated=false;
        this._init();
    }

    ModalWindow.prototype._closeWindow=function(){
        this._modalTrailer.style.display='none';
        this._closeBtn.removeEventListener('click',this._closeBind,false);
    };

    ModalWindow.prototype._createiFrame=function(){
        this._iFrame=document.createElement('iFrame');
        this._iFrame.setAttribute('type','text-html');
        this._videoDiv.appendChild(this._iFrame);
        this._iFrameCreated=true;
    };

    ModalWindow.prototype._playMovie=function(youtubeId){
        if(!this._iFrameCreated){
            this._createiFrame();
        }

        console.log(youtubeId);

        this._iFrame.src='https://www.youtube.com/embed/'+youtubeId+'?autoplay=1&html5=1';
    };

    ModalWindow.prototype.show=function(movieUrl){
        if(this.exists){
            this._modalTrailer.style.display='block';
            this._closeBind=this._closeWindow.bind(this);
            this._closeBtn.addEventListener('click',this._closeBind,false);
            this._playMovie(movieUrl);
        }
    };

    ModalWindow.prototype._getWindowReferences=function(){
        this._modalTrailer=document.getElementsByClassName('modal-window-trailer')[0];
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