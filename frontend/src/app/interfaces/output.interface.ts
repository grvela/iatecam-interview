
export interface CreateOutput {
    amount: number;
    storage_id: number;
    user_id: number;
}

export interface Output extends CreateOutput {
    storage: Storage;
    created_at: Date;
}