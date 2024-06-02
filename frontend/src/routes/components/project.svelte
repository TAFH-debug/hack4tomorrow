<script>
    export let project;
</script>

<a href={"/auth/projects/" + project.id} id={project.id} class="project">
    <img alt="" src={"http://198.211.109.211:8000/images/" + project.image} />
    <div class="project_title">{project.project_name}</div>
    <div class="project_description">{project.project_description}</div>
</a>

<style>
    @import url('https://fonts.googleapis.com/css?family=Poppins:400,500,600,700&display=swap');
    .project {
        border: none;
        outline: none;
        font-family: Poppins, sans-serif;
        display: flex;
        flex-direction: column;
        justify-items: center;
        align-items: center;
        background-color: rgb(220, 220, 220);
        text-decoration: none;
        padding: 20px;
        margin: 15px;
        color: black;
        border-radius: 10px;
        transition: all 0.5s;
        height: 25vw;
        width: 20vw;
    }

    .project:hover {
        color: rgb(39, 39, 39);
        background-color: rgb(195, 195, 195);
    }

    .project_title {
        text-align: center;
        font-size: 20px;
    }

    .project_description {
        text-align: center;
        font-size: 15px;
    }

    .project img {
        width: 80%;
        height: 50%;
        margin: 10px;
    }
</style>