<script>
    import { goto } from '$app/navigation';

    function del() {
        const token = btoa(data.username + ":" + data.password);
        document.getElementById("loading").display = "block";
        fetch("http://165.227.130.2:8000/project/delete", {
            
            method: "POST",
            headers: {
                Authorization: `Basic ${token}`,
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                id: data.id
            })
        }).then((e) => {
            goto("/auth/dashboard")
            document.getElementById("loading").style.display = "none";
        })
    }

    function generate_image() {
        const token = btoa(data.username + ":" + data.password);
        document.getElementById("loading").display = "block";
        fetch("http://165.227.130.2:8000/project/generate_image/", {
            
            method: "POST",
            headers: {
                Authorization: `Basic ${token}`,
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                id: data.id
            })
        }).then((e) => {
            goto("/auth/dashboard")
            document.getElementById("loading").style.display = "none";
        })
    }

    export let data;
</script>

<div class="project" data-sveltekit-reload>
    <img src={"http://165.227.130.2:8000/images/" + data.image} alt=""/>
    <div>
        <div class="project_title">
            {data.project_name}
        </div>
        <div class="project_desc">
            {data.project_description}
        </div>
    </div>
    <div>
        <button class="delete" on:click={del}>Delete</button>
        <button class="generate_image" on:click={generate_image}>Generate image</button>
    </div>
</div>

<style>
    .project {
        border-radius: 20px;
        background-color: white;
        height: 300px;
        width: 80%;
        margin: 0 20px;
        display: flex;
        align-items: center;
    }

    .project_title {
        font-size: 25px;
        font-weight: bold;
    }

    .project img {
        width: 30%;
        aspect-ratio: 1;
        margin: 20px;
    }

    .delete {
        border: none;
        border-radius: 10px;
        background-color: rgb(255, 111, 111);
        color: white;
        margin: 20px;
        padding: 10px;
    }

    .generate_image {
        border: none;
        border-radius: 10px;
        color: white;
        margin: 20px;
        padding: 10px;
        background-color: rgb(121, 255, 121);
    }
</style>