

# class ProductsController < ApplicationController
#   before_action :set_product, only: [:show, :edit, :update, :destroy]
#
#   def index
#     @product = Product.all
#   end
#
#   def show
#
#   end
#
#   def new
#     @product = Product.new
#   end
#
#   def edit
#   end
#
#   def create
#     @product = Product.new(product_params)
#
#     respond_to do |format|
#       if @product.save
#         format.html { redirect_to @product, notice: 'Product was successfully created.' }
#         format.json { render :show, status: :created, location: @product }
#       else
#
#       end
#     end
#   end
# end
#
# def create
#   @product = Product.new(product_params)
#   if true
#     1
#   else
#     2
#   end
# end
#
#
# def show
#   @post = Post.last
#   render :show # <- explicit template to render
# end
#
#
# def show
#   @post = Post.last
#   render :show
# end
#

def adder(first, second)
  first + second
end

puts adder 2, 4


def main a, b, c
  [a, b, c]
end
