<script>
    export let text;
    export let href;
</script>

<a href={href}>{text}</a>

<style>
    a {
        border: none;
        font-family: Outfit, sans-serif;
        text-decoration: none;
        color: rgb(165, 165, 165);
        font-size: 20px;
        transition: all 0.5s;
        background-color: transparent;
        margin: 20px;
        outline: none;
        cursor: pointer;
    }

    a:hover {
        text-shadow: #EEEE00 0 0 10px;
        color: white;
        transform: translate(0, 10px);
    }

</style>