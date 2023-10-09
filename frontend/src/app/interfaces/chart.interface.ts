import { Tag } from "./tag.interface";
import { Product } from "./product.interface";

export interface Chart {
    id: number;
    amount: number;
    product?: Product;
    tag?: Tag;
}

export interface ChartTag extends Chart {
    tag: Tag;
}
