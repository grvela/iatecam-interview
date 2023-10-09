import { Storage } from "./storage.interface";
import { User } from "./user.interface";

export interface Sale {
    id: number;
    amount: number;
    created_at: Date;
    user: User;
    storage: Storage;
}