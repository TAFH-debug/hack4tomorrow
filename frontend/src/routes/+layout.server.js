export async function load({ cookies }) {
    const username = cookies.get("username");
    const password = cookies.get("password");
    const obj = {
        username: "",
        password: "",
        isRegistered: false
    }
    if (username === undefined || password === undefined) return obj;
    
    obj.isRegistered = true;
    return obj;
}
