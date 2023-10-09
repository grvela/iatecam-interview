import { Tag } from "./tag.interface";
import { Product } from "./product.interface";
import { User } from "./user.interface"

export interface Storage {
    id: number;
    user_id: number;
    product_id: number;
    tag_id: number;
    price: number;
    amount: number;
    description: string;
    product: Product;
    tag: Tag;
    user: User
}