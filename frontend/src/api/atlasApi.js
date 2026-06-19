import axios from "axios";

const atlasApi = axios.create({

    baseURL: "http://127.0.0.1:8000"

});

export default atlasApi;