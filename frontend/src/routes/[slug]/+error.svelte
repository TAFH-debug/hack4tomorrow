<script>
    import { page } from "$app/stores";
</script>

<div class="body">
    <h1>
        {$page.status}
    </h1>
    <p>
        {$page.error.message}
    </p>
</div>

<style>
    .body {
        height: 100vh;
        width: 100vw;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        color: white;
    }

    .body * {
        font-size: 80px;
    }
</style>