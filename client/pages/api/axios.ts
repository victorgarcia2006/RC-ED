import axios from "axios";

const instance = axios.create({
    baseURL: 'https://rc-ed-production.up.railway.app/api/monitoreo',
    headers: {
        'Content-Type': 'application/json'
    }
})

export default instance
