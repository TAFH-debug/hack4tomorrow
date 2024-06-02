<script>
    import "$lib/fonts.css";
    
    import { page } from '$app/stores';
    const isError = $page.url.searchParams.has('error');
</script>

<div class="login_container">
    <form method="POST">
        <div class="form-row">
            <div class="input-data">
                <input name="username" id="username" type="text" required>
                <div class="underline"></div>
                <label for="">Username</label>
            </div>
        </div>
        <div class="form-row">
            <div class="input-data">
                <input name="password" id="password" type="password" required>
                <div class="underline"></div>
                <label for="">Password</label>
            </div>
        </div>
        <div class="form-row submit-btn">
            <div class="input-data">
               <input type="submit" value="submit">
            </div>
         </div>
         {#if isError}
         <div class="form-row error">
            Invalid data
         </div>
         {/if}
    </form>
</div>

<style>
    @import url('https://fonts.googleapis.com/css?family=Poppins:400,500,600,700&display=swap');
    *{
        margin: 0;
        padding: 0;
        outline: none;
        box-sizing: border-box;
        font-family: 'Poppins', sans-serif;
    }

    .error {
        color: red;
        margin: 20px;
    }

    .login_container {
        display: flex;
        justify-content: center;
        flex-direction: column;
        align-items: center;
        width: 100vw;
        height: 100vh;
    }

    form {
        width: 30vw;
        background-color: white;
        border-radius: 20px;
        display: flex;
        flex-direction: column;
    }

    form .form-row .input-data {
        width: 100%;
        height: 40px;
        margin: 20px;
        position: relative;
    }
    
    .input-data input {
        display: block;
        width: 80%;
        height: 100%;
        border: none;
        font-size: 17px;
        border-bottom: 2px solid rgba(0,0,0, 0.12);
    }

    .input-data input:focus ~ label, 
    .input-data input:valid ~ label {
        transform: translateY(-20px);
        font-size: 14px;
        color: #3498db;
    }

    .input-data label{
        position: absolute;
        pointer-events: none;
        bottom: 10px;
        font-size: 16px;
        transition: all 0.3s ease;
    }

    .input-data .underline{
        position: absolute;
        bottom: 0;
        height: 2px;
        width: 80%;
    }

    .input-data .underline:before{
        position: absolute;
        content: "";
        height: 2px;
        width: 100%;
        background: #3498db;
        transform: scaleX(0);
        transform-origin: center;
        transition: transform 0.3s ease;
    }

    .input-data input:focus ~ .underline:before,
    .input-data input:valid ~ .underline:before {
        transform: scale(1);
    }

    .submit-btn .input-data input {
        background: none;
        border: none;
        color: #fff;
        font-size: 17px;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 1px;
        cursor: pointer;
        position: relative;
        z-index: 2;
        background-color: black;
        border-radius: 10px;
    }

    .submit-btn .input-data input:hover {
        background-color: rgb(49, 49, 49);
    }
</style>