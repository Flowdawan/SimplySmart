export default class Timer{
    //pass here the things were in html
    constructor(root) {
        root.innerHTML= Timer.getHTML();

        this.element = {
            minutes: root.querySelector(".timer__part--minutes"),
            seconds: root.querySelector(".timer__part--seconds"),
            control: root.querySelector(".timer__btn--control"),
            reset: root.querySelector(".timer__btn--reset")
        };
        //no interval so the timer will not be running but i want to trigger it with set interval
        this.interval = null;
        // this will be the seconds as 0 by default
        this.remainingSeconds= 0;

        this.element.control.addEventListener("click",() =>{
            if (this.interval=== null){
                this.start();
            }
            else {
                this.stop();
            }
        });
        this.element.reset.addEventListener("click",() =>{
            const inputMinutes = prompt("Enter number of minutes");

            if (inputMinutes < 60){
                this.stop();

                // to convert our time into seconds
                this.remainingSeconds= inputMinutes*60;
                this.updateInterfaceTime();
            }
        });
    }

    updateInterfaceTime(){
        //to show for example what 90 seconds are in minutes and the remaining 30 seconds in seconds
        const minutes= Math.floor(this.remainingSeconds /60);
        const seconds = this.remainingSeconds % 60;
        this.element.minutes.textContent= minutes.toString().padStart(2,"0"); //to pad the beginnng of our string to be zero if ther is only one number. to put a zero ex: 01min
        this.element.seconds.textContent= seconds.toString().padStart(2,"0");
    }

    updateInterfaceControls(){
        if (this.interval === null){
            this.element.control.innerHTML= `<span class="material-icons">play_arrow </span>`;
            this.element.control.classList.add("timer__btn--start");
            //for the stop button
            this.element.control.classList.remove("timer__btn--stop");
        }
        else{
            this.element.control.innerHTML= `<span class="material-icons">pause</span>`;
            this.element.control.classList.add("timer__btn--stop");
            this.element.control.classList.remove("timer__btn--start");
        }

    }
    
    start(){
        //cancel current operation
        if (this.remainingSeconds===0)
            return;

        //run code on timer in ms
        this.interval= setInterval(()=> {
            this.remainingSeconds--;
            this.updateInterfaceTime();

            if(this.remainingSeconds===0){
                this.stop();
            }
        }, 1000);
        //to desplay and swap the bottons
        this.updateInterfaceControls();
    }

    stop(){
        //to stop the interval
        clearInterval(this.interval);
        this.interval = null;
        this.updateInterfaceControls();
    }

    //method for returning the html string for inside the timer
    static getHTML(){
        return `
        <span class="timer__part timer__part--minutes">00</span>
        <span class="timer__part">:</span>
        <span class="timer__part timer__part--seconds">00</span>
        <button type="button" class="timer__btn timer__btn--control timer__btn--start">
          <span class="material-icons">play_arrow</span>
        </button>
        <button type="button" class="timer__btn timer__btn--control timer__btn--reset">
          <span class="material-icons">timer</span>
        </button>
        `
    }

}