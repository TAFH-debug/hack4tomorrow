<script>
    import "$lib/fonts.css";
    export let data;
</script>

<div class="container">
    <div class="sidebar" data-sveltekit-reload>
        <a href={"/auth/projects/" + data.slug}>Project</a>
        <a href={"/auth/projects/" + data.slug + "/characters/"}>Characters</a>
        <a href={"/auth/projects/" + data.slug + "/concept_arts/"}>Concept Arts</a>
        <a href={"/auth/projects/" + data.slug + "/dialogs/"}>Dialogs</a>
        <a href={"/auth/projects/" + data.slug + "/assets/"}>Assets</a>
    </div>
    <slot />
</div>

<style>
    .container {
        width: 100%;
        display: flex;
        margin: 10px;
    }

    .sidebar {
        width: 20%;
        display: flex;
        flex-direction: column;
        background-color: white;
        border-radius: 20px;
        color: black;
        font-family: Outfit, sans-serif;
    }

    .sidebar a {
        width: 100%;
        color: black;
        text-align: center;
        margin: 10px;
        text-decoration: none;
        font-size: 20px;
        transition: all 0.5s;
    }

    .sidebar a:hover {
        transform: scale(1.1);
    }
</style>