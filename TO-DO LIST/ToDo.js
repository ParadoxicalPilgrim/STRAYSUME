function addTask(){
    let taskInput=document.getElementById("taskInput");
    let taskList=document.getElementById("taskList");
    let taskContent=taskInput.value.trim();

    if (taskContent===''){
        alert(`Please enter a task.`);
        return;
    }

    const li=document.createElement('li');
    li.textContent=taskContent;

    //ADDING DELETE BUTTON

    const deleteBtn=document.createElement('button');
    deleteBtn.textContent='X';
    deleteBtn.style.color='#ff0000';
    deleteBtn.style.padding='5px';
    deleteBtn.style.width='30px';
    deleteBtn.style.height='30px';
    deleteBtn.style.border="0px";
    deleteBtn.style.borderRadius='50%';
    deleteBtn.style.marginLeft="7px";
    deleteBtn.style.backgroundColor='#ffffff';


    deleteBtn.onclick=function(){
        taskList.removeChild(li);
    }
    
    li.appendChild(deleteBtn);
    taskList.appendChild(li);
    taskInput.value='';
}


// ADDING THE EVENT LISTENER TO THE ADD TASK BUTTON

document.getElementById("addTaskBtn").addEventListener('click',function(){
    addTask();
});

// ADDING THE EVENT LISTENER BY PRESSING THE ENTER KEY

document.getElementById("taskInput").addEventListener('keypress',function(e){
    if (e.key==='Enter'){
        addTask();
    }
})

// DARK MODE 

document.getElementById("themeToggle").addEventListener('click',function(){
    let dark=document.getElementsByClassName('light-mode');
    if (dark.length>0){
        document.body.classList.toggle('dark-mode');
    }
});